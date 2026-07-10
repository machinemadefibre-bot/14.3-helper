param(
    [string]$GameDir = "S:\SteamLibrary\steamapps\common\World of Warships",
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$WowsUnpack = "",
    [string]$GameParamsJson = "",
    [string]$Realm = "",
    [string]$ShipKeyFilter = "",
    [string]$GeometryDir = "",
    [string]$PatchVersion = "",
    [string]$TargetGameVersion = "",
    [string]$ExpectedGameBuild = "",
    [string]$Python = "",
    [int]$MaxShips = 0,
    [int]$MaxChangedShips = 0,
    [int]$MaxChangedFields = 0,
    [double]$MaxShipCountDeltaPercent = 10,
    [double]$MaxRemovedPercent = 5,
    [double]$MaxDiffPercent = 25,
    [switch]$NoExtractGameParams,
    [switch]$SkipGeometryRefine,
    [switch]$AllowUnrefinedDatabase,
    [switch]$AutoApply,
    [switch]$FullTest,
    [switch]$NoPause,
    [switch]$SelfTest,
    [ValidateSet("", "menu", "update", "edit", "mainbelt")]
    [string]$Mode = ""
)

$ErrorActionPreference = "Stop"

try {
    chcp.com 65001 | Out-Null
    $utf8 = New-Object System.Text.UTF8Encoding $false
    [Console]::InputEncoding = $utf8
    [Console]::OutputEncoding = $utf8
    $OutputEncoding = $utf8
} catch {
    # Encoding setup is best-effort; the workflow itself does not depend on it.
}

function Pause-IfNeeded {
    if (-not $NoPause) {
        Write-Host ""
        [void](Read-Host "Press Enter to exit")
    }
}

function As-Array {
    param($Value)
    if ($null -eq $Value) { return @() }
    if ($Value -is [System.Array]) { return @($Value) }
    return @($Value)
}

function Format-Value {
    param($Value)
    if ($null -eq $Value) { return "" }
    if ($Value -is [System.Array]) {
        return ((@($Value) | ForEach-Object { [string]$_ }) -join ",")
    }
    return [string]$Value
}

function Read-JsonFile {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return $null }
    return Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json
}

function Get-MetaValue {
    param($Database, [string]$Name)
    if ($null -eq $Database -or $null -eq $Database.meta) { return "" }
    $prop = $Database.meta.PSObject.Properties[$Name]
    if ($prop) { return [string]$prop.Value }
    return ""
}

function ConvertTo-SafeNamePart {
    param([string]$Value)
    $safe = ([string]$Value).Trim() -replace '[^A-Za-z0-9._-]+', '_'
    return $safe.Trim("_")
}

function Get-ConstantValue {
    param([string]$Name)
    $constantsPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_constants.py"
    if (-not (Test-Path -LiteralPath $constantsPath)) { return "" }
    $text = Get-Content -LiteralPath $constantsPath -Raw -Encoding UTF8
    if ($text -match "(?m)^\s*$([regex]::Escape($Name))\s*=\s*'([^']*)'") {
        return $Matches[1]
    }
    return ""
}

function Get-ModVersionNamePart {
    $version = Get-ConstantValue "MOD_VERSION"
    if (-not $version) { return "" }
    if ($version.StartsWith("v", [System.StringComparison]::OrdinalIgnoreCase)) { return $version }
    return "v$version"
}

function Get-TargetGameVersion {
    return Get-ConstantValue "TARGET_GAME_VERSION"
}

function Set-TargetGameVersion {
    param([string]$Version)
    if (-not $Version) { return }

    $constantsPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_constants.py"
    if (-not (Test-Path -LiteralPath $constantsPath)) {
        throw "Constants file not found: $constantsPath"
    }

    $text = Get-Content -LiteralPath $constantsPath -Raw -Encoding UTF8
    $pattern = "(?m)^\s*TARGET_GAME_VERSION\s*=.*$"
    if ($text -notmatch $pattern) {
        throw "TARGET_GAME_VERSION was not found in $constantsPath"
    }

    $updated = [regex]::Replace($text, $pattern, "TARGET_GAME_VERSION = '$Version'", 1)
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($constantsPath, $updated, $utf8NoBom)
    Write-Host ("Target game version: {0}" -f $Version)
}

function Get-LatestDiffFile {
    param([string]$UpdateDir, [datetime]$RunStart)
    $recent = @(
        Get-ChildItem -LiteralPath $UpdateDir -Filter "armor_diff.*.json" -ErrorAction SilentlyContinue |
            Where-Object { $_.LastWriteTime -ge $RunStart.AddSeconds(-10) } |
            Sort-Object LastWriteTime -Descending
    )
    if ($recent.Count -gt 0) { return $recent[0].FullName }

    $latest = @(
        Get-ChildItem -LiteralPath $UpdateDir -Filter "armor_diff.*.json" -ErrorAction SilentlyContinue |
            Sort-Object LastWriteTime -Descending
    )
    if ($latest.Count -gt 0) { return $latest[0].FullName }
    return ""
}

function Show-ShipList {
    param([string]$Title, $Ships, [ConsoleColor]$Color, [string]$Prefix = "+")
    Write-Host ""
    Write-Host $Title -ForegroundColor $Color
    $items = As-Array $Ships
    if ($items.Count -eq 0) {
        Write-Host "  none"
        return
    }
    foreach ($ship in $items) {
        Write-Host ("  {0} {1} | {2} | caliber {3}" -f $Prefix, $ship.key, $ship.name, $ship.mainGunCaliberMm)
    }
}

function Show-ChangedShips {
    param($Changed)
    Write-Host ""
    Write-Host "Changed ships" -ForegroundColor Yellow
    $ships = As-Array $Changed
    if ($ships.Count -eq 0) {
        Write-Host "  none"
        return
    }

    $shownShips = 0
    $shownFields = 0
    foreach ($ship in $ships) {
        if ($MaxChangedShips -gt 0 -and $shownShips -ge $MaxChangedShips) {
            Write-Host ("  ... {0} more changed ships hidden" -f ($ships.Count - $shownShips))
            break
        }
        $shownShips += 1
        Write-Host ("  * {0} | {1}" -f $ship.key, $ship.name)

        foreach ($field in (As-Array $ship.fields)) {
            if ($MaxChangedFields -gt 0 -and $shownFields -ge $MaxChangedFields) {
                Write-Host "    ... more changed fields hidden"
                return
            }
            $shownFields += 1
            Write-Host ("    - {0}: {1} -> {2}" -f $field.field, (Format-Value $field.old), (Format-Value $field.new))
        }
    }
}

function Show-Diff {
    param($Diff, [string]$DiffPath)
    $added = As-Array $Diff.added
    $removed = As-Array $Diff.removed
    $changed = As-Array $Diff.changed

    Write-Host ""
    Write-Host "================ Armor DB diff ================" -ForegroundColor Cyan
    Write-Host ("Old build: {0}    New build: {1}" -f $Diff.meta.oldBuild, $Diff.meta.newBuild)
    Write-Host ("Old ships: {0}    New ships: {1}" -f $Diff.meta.oldShipCount, $Diff.meta.newShipCount)
    Write-Host ("Added: {0}    Removed: {1}    Changed: {2}" -f $added.Count, $removed.Count, $changed.Count)
    Write-Host ("Diff file: {0}" -f $DiffPath)
    Write-Host ("Candidate: {0}" -f $Diff.meta.candidatePath)

    Show-ShipList "Added ships" $added Green "+"
    Show-ShipList "Removed ships" $removed Red "-"
    Show-ChangedShips $changed
    Write-Host "================================================" -ForegroundColor Cyan
}

function Assert-AutomationDiffSafe {
    param($Diff)
    if (-not $AutoApply) { return }

    $oldBuild = [string]$Diff.meta.oldBuild
    $newBuild = [string]$Diff.meta.newBuild
    if ($ExpectedGameBuild -and $newBuild -ne $ExpectedGameBuild) {
        throw "AUTOMATION_DIFF_UNSAFE: candidate build $newBuild does not match installed build $ExpectedGameBuild"
    }

    $oldCount = [double]$Diff.meta.oldShipCount
    $newCount = [double]$Diff.meta.newShipCount
    if ($oldCount -le 0 -or $newCount -le 0) {
        throw "AUTOMATION_DIFF_UNSAFE: invalid ship counts old=$oldCount new=$newCount"
    }

    $addedCount = (As-Array $Diff.added).Count
    $removedCount = (As-Array $Diff.removed).Count
    $changedCount = (As-Array $Diff.changed).Count
    $shipDeltaPercent = ([math]::Abs($newCount - $oldCount) / $oldCount) * 100
    $removedPercent = ($removedCount / $oldCount) * 100
    $diffPercent = (($addedCount + $removedCount + $changedCount) / $oldCount) * 100

    if ($shipDeltaPercent -gt $MaxShipCountDeltaPercent) {
        throw ("AUTOMATION_DIFF_UNSAFE: ship-count delta {0:N2}% exceeds {1:N2}%" -f $shipDeltaPercent, $MaxShipCountDeltaPercent)
    }
    if ($removedPercent -gt $MaxRemovedPercent) {
        throw ("AUTOMATION_DIFF_UNSAFE: removed ships {0:N2}% exceeds {1:N2}%" -f $removedPercent, $MaxRemovedPercent)
    }
    if ($diffPercent -gt $MaxDiffPercent) {
        throw ("AUTOMATION_DIFF_UNSAFE: total diff {0:N2}% exceeds {1:N2}%" -f $diffPercent, $MaxDiffPercent)
    }

    Write-Host ("Automation safety: build {0}->{1}, ship delta {2:N2}%, removed {3:N2}%, total diff {4:N2}%" -f `
        $oldBuild, $newBuild, $shipDeltaPercent, $removedPercent, $diffPercent)
}

function Read-Confirmation {
    param([string]$Prompt)
    while ($true) {
        $answer = (Read-Host "$Prompt [Y/N]").Trim()
        if ($answer -match '^(Y|YES)$') { return $true }
        if ($answer -match '^(N|NO)?$') { return $false }
        Write-Host "Please type Y or N."
    }
}

function Read-PatchVersionOrDefault {
    param([string]$DefaultValue)

    if ($PatchVersion) { return $PatchVersion }
    if (-not [Console]::IsInputRedirected) {
        Write-Host ""
        $answer = (Read-Host "Patch version for zip suffix (Enter for $DefaultValue)").Trim()
        if ($answer) { return $answer }
    }
    return $DefaultValue
}

function Apply-CandidateDatabase {
    param([string]$CandidatePath)
    if (-not (Test-Path -LiteralPath $CandidatePath)) {
        throw "Candidate database not found: $CandidatePath"
    }

    $dataPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
    $snapshotDir = Join-Path $ProjectRoot "tools\armor_snapshots"
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    New-Item -ItemType Directory -Force -Path $snapshotDir | Out-Null

    if (Test-Path -LiteralPath $dataPath) {
        $oldDb = Read-JsonFile $dataPath
        $oldBuild = Get-MetaValue $oldDb "gameBuild"
        if (-not $oldBuild) { $oldBuild = "unknown-build" }
        $backupPath = Join-Path $snapshotDir ("armor_overmatch.{0}.{1}.json" -f (ConvertTo-SafeNamePart $oldBuild), $timestamp)
        Copy-Item -LiteralPath $dataPath -Destination $backupPath -Force
        Write-Host ("Backed up old database: {0}" -f $backupPath)
    }

    Copy-Item -LiteralPath $CandidatePath -Destination $dataPath -Force
    Write-Host ("Applied database: {0}" -f $dataPath)

    $candidatePyPath = [System.IO.Path]::ChangeExtension($CandidatePath, ".py")
    $dataPyPath = [System.IO.Path]::ChangeExtension($dataPath, ".py")
    if (Test-Path -LiteralPath $candidatePyPath) {
        Copy-Item -LiteralPath $candidatePyPath -Destination $dataPyPath -Force
        Write-Host ("Applied Python database: {0}" -f $dataPyPath)
    }
}

function Invoke-Checked {
    param([string]$FilePath, [string[]]$Arguments)
    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$FilePath failed with exit code $LASTEXITCODE"
    }
}

function Get-UsableNode {
    $candidatePaths = @(
        (Join-Path $ProjectRoot ".tools\node\node.exe"),
        (Join-Path $ProjectRoot "tools\node\node.exe")
    )
    $candidatePaths += @(Get-Command node -All -ErrorAction SilentlyContinue | ForEach-Object { $_.Source })

    foreach ($candidatePath in ($candidatePaths | Where-Object { $_ } | Select-Object -Unique)) {
        if (-not (Test-Path -LiteralPath $candidatePath)) { continue }
        try {
            & $candidatePath --version *> $null
            if ($LASTEXITCODE -eq 0) { return $candidatePath }
        } catch {
            continue
        }
    }

    return ""
}

function Get-UsablePython {
    $candidatePaths = @()
    if ($Python) { $candidatePaths += $Python }
    $candidatePaths += @(
        (Join-Path $ProjectRoot ".tools\python\python.exe"),
        (Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe")
    )
    $candidatePaths += @(Get-Command python -All -ErrorAction SilentlyContinue | ForEach-Object { $_.Source })

    foreach ($candidatePath in ($candidatePaths | Where-Object { $_ } | Select-Object -Unique)) {
        if (-not (Test-Path -LiteralPath $candidatePath)) { continue }
        try {
            & $candidatePath --version *> $null
            if ($LASTEXITCODE -eq 0) { return (Resolve-Path -LiteralPath $candidatePath).Path }
        } catch {
            continue
        }
    }

    return ""
}

function Invoke-FullTestAndBuild {
    param([string]$TestScript)

    $pythonPath = Get-UsablePython
    if (-not $pythonPath) {
        throw "Python is required for unattended full tests. Keep the Codex runtime available or pass -Python."
    }

    Write-Host ""
    Write-Host ("Running full tests with {0}..." -f $pythonPath)
    $testOutput = @(Invoke-Checked "powershell" @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $TestScript,
        "-Python", $pythonPath,
        "-Build"
    ))
    foreach ($line in $testOutput) { Write-Host $line }

    $packagePatchVersion = ConvertTo-SafeNamePart (Get-TargetGameVersion)
    $modVersionNamePart = ConvertTo-SafeNamePart (Get-ModVersionNamePart)
    $packageNamePrefix = if ($modVersionNamePart) { "14.3-helper_$modVersionNamePart" } else { "14.3-helper" }
    $zipPath = Join-Path (Join-Path $ProjectRoot "dist") "${packageNamePrefix}_Aslain-patch$packagePatchVersion.zip"
    if (-not (Test-Path -LiteralPath $zipPath)) {
        throw "Full tests completed without the expected package: $zipPath"
    }
    return $zipPath
}

function Read-ToolMode {
    while ($true) {
        Write-Host ""
        Write-Host "AP Overmatch armor tool" -ForegroundColor Cyan
        Write-Host "  1. Update armor database and build package"
        Write-Host "  2. Manually edit armor database"
        Write-Host "  3. Extract main belt geometry"
        Write-Host "  4. Exit"
        $answer = (Read-Host "Select option [1]").Trim()
        if (-not $answer -or $answer -eq "1") { return "update" }
        if ($answer -eq "2") { return "edit" }
        if ($answer -eq "3") { return "mainbelt" }
        if ($answer -eq "4" -or $answer -match '^(Q|QUIT|EXIT)$') { return "exit" }
        Write-Host "Please select 1, 2, 3, or 4."
    }
}

function Get-CurrentDatabaseBuild {
    $targetVersion = Get-TargetGameVersion
    if ($targetVersion) { return $targetVersion }

    $dataPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
    $db = Read-JsonFile $dataPath
    $build = Get-MetaValue $db "gameBuild"
    if ($build) { return $build }
    return "manual"
}

function Invoke-BuildPackage {
    param([string]$DefaultPatchVersion, [string]$BuildScript)

    $packagePatchVersion = Read-PatchVersionOrDefault $DefaultPatchVersion
    $packagePatchVersion = ConvertTo-SafeNamePart $packagePatchVersion
    if (-not $packagePatchVersion) { throw "Unable to determine patch version for zip name." }

    Write-Host ""
    Write-Host ("Building Aslain package for patch {0}..." -f $packagePatchVersion)
    Invoke-Checked "powershell" @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $BuildScript,
        "-ProjectRoot", $ProjectRoot,
        "-PatchVersion", $packagePatchVersion
    )

    $modVersionNamePart = ConvertTo-SafeNamePart (Get-ModVersionNamePart)
    $packageNamePrefix = if ($modVersionNamePart) { "14.3-helper_$modVersionNamePart" } else { "14.3-helper" }
    $zipPath = Join-Path (Join-Path $ProjectRoot "dist") "${packageNamePrefix}_Aslain-patch$packagePatchVersion.zip"
    Write-Host ""
    Write-Host ("Done: {0}" -f $zipPath) -ForegroundColor Green
}

function Invoke-UnboundArmorDbGeneration {
    $script = Join-Path $ProjectRoot "tools\generate-unbound-armor-db.mjs"
    if (-not (Test-Path -LiteralPath $script)) {
        throw "Unbound armor DB generator not found: $script"
    }

    $node = Get-UsableNode
    if (-not $node) {
        throw "Node.js is required to sync the Unbound armor database. Put node.exe under .tools\node or install Node.js."
    }

    & $node $script
    if ($LASTEXITCODE -ne 0) {
        throw "generate-unbound-armor-db.mjs failed with exit code $LASTEXITCODE"
    }
}

function Resolve-CurrentGameParamsJson {
    if ($GameParamsJson) {
        if (-not (Test-Path -LiteralPath $GameParamsJson)) { throw "GameParams JSON not found: $GameParamsJson" }
        return (Resolve-Path $GameParamsJson).Path
    }

    $dataPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
    $db = Read-JsonFile $dataPath
    $build = Get-MetaValue $db "gameBuild"
    $dbRealm = Get-MetaValue $db "realm"
    $realmName = if ($Realm) { $Realm } elseif ($dbRealm) { $dbRealm } else { "ASIA" }
    $candidates = @()
    if ($build -and $realmName) { $candidates += Join-Path $ProjectRoot "build\gameparams\GameParams_$($build)_$($realmName).json" }
    if ($build) { $candidates += Join-Path $ProjectRoot "build\gameparams\GameParams_$($build).json" }
    if ($realmName) { $candidates += Join-Path $ProjectRoot "build\gameparams\GameParams_$($realmName).json" }

    foreach ($candidate in $candidates) {
        if (Test-Path -LiteralPath $candidate) { return (Resolve-Path $candidate).Path }
    }
    throw "GameParams JSON not found. Provide -GameParamsJson or run option 1 first."
}

function Invoke-MainBeltExtraction {
    param([string]$TestScript, [string]$BuildScript)

    $node = Get-UsableNode
    if (-not $node) {
        throw "Node.js is required for main belt extraction. Put node.exe under .tools\node or install Node.js."
    }

    $script = Join-Path $ProjectRoot "tools\refine-side-from-geometry.mjs"
    if (-not (Test-Path -LiteralPath $script)) {
        throw "Main belt extraction script not found: $script"
    }

    $dataPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
    $gameParamsPath = Resolve-CurrentGameParamsJson
    $resolvedGeometryDir = if ($GeometryDir) { $GeometryDir } else { Join-Path $ProjectRoot "build\scratch\ship_geometry_flat" }
    if (-not (Test-Path -LiteralPath $resolvedGeometryDir)) {
        throw "Geometry directory not found: $resolvedGeometryDir"
    }

    $snapshotDir = Join-Path $ProjectRoot "tools\armor_snapshots"
    New-Item -ItemType Directory -Force -Path $snapshotDir | Out-Null
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backupPath = Join-Path $snapshotDir ("armor_overmatch.mainbelt.{0}.json" -f $timestamp)
    Copy-Item -LiteralPath $dataPath -Destination $backupPath -Force
    Write-Host ("Backed up old database: {0}" -f $backupPath)

    Write-Host "Extracting main belt geometry..."
    & $node $script "--db" $dataPath "--game-params" $gameParamsPath "--geometry-dir" $resolvedGeometryDir "--main-belt-only"
    if ($LASTEXITCODE -ne 0) {
        throw "refine-side-from-geometry.mjs failed with exit code $LASTEXITCODE"
    }

    Invoke-UnboundArmorDbGeneration

    $db = Read-JsonFile $dataPath
    $yamato = if ($db.ships) { $db.ships.PSObject.Properties["PJSB018_Yamato_1944"].Value } else { $null }
    if ($yamato -and $yamato.armor -and $yamato.armor.mainBelt) {
        $belt = $yamato.armor.mainBelt
        Write-Host ("Yamato main belt: {0} mm, inclination {1}-{2} deg, heading angle {3}-{4} deg" -f `
            ((As-Array $belt.values) -join "/"), `
            $belt.inclinationDeg.min, $belt.inclinationDeg.max, `
            $belt.headingAngleDeg.min, $belt.headingAngleDeg.max)
    }

    if (Read-Confirmation "Run rule tests and build package now?") {
        Write-Host ""
        Write-Host "Running rule tests..."
        Invoke-Checked "powershell" @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $TestScript)
        Invoke-BuildPackage (Get-CurrentDatabaseBuild) $BuildScript
    } else {
        Write-Host "Main belt extraction finished. Database was changed, package was not built."
    }
}

function Invoke-ManualEditor {
    param([string]$EditorScript, [string]$TestScript, [string]$BuildScript)

    if (-not (Test-Path -LiteralPath $EditorScript)) {
        throw "Manual editor script not found: $EditorScript"
    }

    $node = Get-UsableNode
    if (-not $node) {
        throw "Node.js is required for the manual editor. Put node.exe under .tools\node or install Node.js."
    }

    $dataPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
    & $node $EditorScript "--db" $dataPath
    if ($LASTEXITCODE -ne 0) {
        throw "manual-edit-armor-db.mjs failed with exit code $LASTEXITCODE"
    }

    Invoke-UnboundArmorDbGeneration

    if (Read-Confirmation "Run rule tests and build package now?") {
        Write-Host ""
        Write-Host "Running rule tests..."
        Invoke-Checked "powershell" @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $TestScript)
        Invoke-BuildPackage (Get-CurrentDatabaseBuild) $BuildScript
    } else {
        Write-Host "Manual edit finished. Database was changed, package was not built."
    }
}

$exitCode = 0
try {
    $ProjectRoot = (Resolve-Path $ProjectRoot).Path
    $updateScript = Join-Path $PSScriptRoot "update-armor-db.ps1"
    $manualEditorScript = Join-Path $PSScriptRoot "manual-edit-armor-db.mjs"
    $testScript = Join-Path $PSScriptRoot "test-rule.ps1"
    $fullTestScript = Join-Path $PSScriptRoot "test.ps1"
    $buildScript = Join-Path $PSScriptRoot "build.ps1"
    $updateDir = Join-Path $ProjectRoot "build\armor-update"

    foreach ($required in @($updateScript, $testScript, $fullTestScript, $buildScript)) {
        if (-not (Test-Path -LiteralPath $required)) { throw "Required script not found: $required" }
    }

    if ($SelfTest) {
        Write-Host "Self-test OK."
        Write-Host ("ProjectRoot: {0}" -f $ProjectRoot)
        Write-Host ("GameDir: {0}" -f $GameDir)
        Write-Host ("Update script: {0}" -f $updateScript)
        Write-Host ("Manual editor: {0}" -f $manualEditorScript)
        Write-Host ("Auto apply: {0}" -f $AutoApply)
        return
    }

    $selectedMode = $Mode
    if (-not $selectedMode) {
        if (-not [Console]::IsInputRedirected -and $PSBoundParameters.Count -eq 0) {
            $selectedMode = Read-ToolMode
        } else {
            $selectedMode = "update"
        }
    } elseif ($selectedMode -eq "menu") {
        $selectedMode = Read-ToolMode
    }

    if ($selectedMode -eq "exit") { return }
    if ($selectedMode -eq "edit") {
        Invoke-ManualEditor $manualEditorScript $testScript $buildScript
        return
    }
    if ($selectedMode -eq "mainbelt") {
        Invoke-MainBeltExtraction $testScript $buildScript
        return
    }

    if ($AutoApply) {
        if (-not $ExpectedGameBuild) { throw "-ExpectedGameBuild is required with -AutoApply." }
        if (-not $TargetGameVersion) { throw "-TargetGameVersion is required with -AutoApply." }
        if (-not $PatchVersion) { throw "-PatchVersion is required with -AutoApply." }
    }

    Write-Host "Generating candidate armor database..."
    $runStart = Get-Date
    $updateArgs = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $updateScript,
        "-GameDir", $GameDir,
        "-ProjectRoot", $ProjectRoot
    )
    if ($WowsUnpack) { $updateArgs += @("-WowsUnpack", $WowsUnpack) }
    if ($GameParamsJson) { $updateArgs += @("-GameParamsJson", $GameParamsJson) }
    if ($Realm) { $updateArgs += @("-Realm", $Realm) }
    if ($ShipKeyFilter) { $updateArgs += @("-ShipKeyFilter", $ShipKeyFilter) }
    if ($GeometryDir) { $updateArgs += @("-GeometryDir", $GeometryDir) }
    if ($MaxShips -gt 0) { $updateArgs += @("-MaxShips", [string]$MaxShips) }
    if (-not $NoExtractGameParams) { $updateArgs += "-ExtractGameParams" }
    if ($SkipGeometryRefine) { $updateArgs += "-SkipGeometryRefine" }
    if ($AllowUnrefinedDatabase) { $updateArgs += "-AllowUnrefinedDatabase" }

    Invoke-Checked "powershell" $updateArgs

    $diffPath = Get-LatestDiffFile $updateDir $runStart
    if (-not $diffPath) { throw "No armor diff JSON was created under $updateDir" }
    $diff = Read-JsonFile $diffPath
    if ($null -eq $diff) { throw "Unable to read diff JSON: $diffPath" }

    Show-Diff $diff $diffPath
    Assert-AutomationDiffSafe $diff

    $addedCount = (As-Array $diff.added).Count
    $removedCount = (As-Array $diff.removed).Count
    $changedCount = (As-Array $diff.changed).Count
    $hasChanges = ($addedCount + $removedCount + $changedCount) -gt 0
    $buildChanged = ([string]$diff.meta.oldBuild) -ne ([string]$diff.meta.newBuild)
    $shouldApplyCandidate = $hasChanges -or $buildChanged

    if ($AutoApply) {
        $confirmed = $true
        Write-Host "AutoApply accepted the validated candidate."
    } elseif ($hasChanges -or $buildChanged) {
        $confirmed = Read-Confirmation "Apply this database update and build patch package?"
    } else {
        $confirmed = Read-Confirmation "No database changes found. Build patch package anyway?"
    }

    if (-not $confirmed) {
        Write-Host "Cancelled. Database was not changed and no package was built."
        return
    }

    if ($shouldApplyCandidate) {
        Apply-CandidateDatabase ([string]$diff.meta.candidatePath)
        Invoke-UnboundArmorDbGeneration
    } else {
        Write-Host "Keeping current database."
    }

    if ($TargetGameVersion) {
        Set-TargetGameVersion $TargetGameVersion
    }

    if ($AutoApply -or $FullTest) {
        $zipPath = Invoke-FullTestAndBuild $fullTestScript
        Write-Host ""
        Write-Host ("Done: {0}" -f $zipPath) -ForegroundColor Green
    } else {
        Write-Host ""
        Write-Host "Running rule tests..."
        Invoke-Checked "powershell" @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $testScript)
        Invoke-BuildPackage ([string]$diff.meta.newBuild) $buildScript
    }
} catch {
    $exitCode = 1
    Write-Host ""
    Write-Host ("ERROR: {0}" -f $_.Exception.Message) -ForegroundColor Red
} finally {
    Pause-IfNeeded
    if ($exitCode -ne 0) { exit $exitCode }
}
