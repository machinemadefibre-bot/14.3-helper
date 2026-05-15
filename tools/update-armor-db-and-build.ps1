param(
    [string]$GameDir = "S:\SteamLibrary\steamapps\common\World of Warships",
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$WowsUnpack = "",
    [string]$GameParamsJson = "",
    [string]$Realm = "",
    [string]$ShipKeyFilter = "",
    [string]$GeometryDir = "",
    [string]$PatchVersion = "",
    [int]$MaxShips = 0,
    [int]$MaxChangedShips = 0,
    [int]$MaxChangedFields = 0,
    [switch]$NoExtractGameParams,
    [switch]$SkipGeometryRefine,
    [switch]$NoPause,
    [switch]$SelfTest
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
    Write-Host "Changed ships / 变化" -ForegroundColor Yellow
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

    Show-ShipList "Added ships / 新增" $added Green "+"
    Show-ShipList "Removed ships / 删除" $removed Red "-"
    Show-ChangedShips $changed
    Write-Host "================================================" -ForegroundColor Cyan
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

$exitCode = 0
try {
    $ProjectRoot = (Resolve-Path $ProjectRoot).Path
    $updateScript = Join-Path $PSScriptRoot "update-armor-db.ps1"
    $testScript = Join-Path $PSScriptRoot "test-rule.ps1"
    $buildScript = Join-Path $PSScriptRoot "build.ps1"
    $updateDir = Join-Path $ProjectRoot "build\armor-update"

    foreach ($required in @($updateScript, $testScript, $buildScript)) {
        if (-not (Test-Path -LiteralPath $required)) { throw "Required script not found: $required" }
    }

    if ($SelfTest) {
        Write-Host "Self-test OK."
        Write-Host ("ProjectRoot: {0}" -f $ProjectRoot)
        Write-Host ("GameDir: {0}" -f $GameDir)
        Write-Host ("Update script: {0}" -f $updateScript)
        return
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

    Invoke-Checked "powershell" $updateArgs

    $diffPath = Get-LatestDiffFile $updateDir $runStart
    if (-not $diffPath) { throw "No armor diff JSON was created under $updateDir" }
    $diff = Read-JsonFile $diffPath
    if ($null -eq $diff) { throw "Unable to read diff JSON: $diffPath" }

    Show-Diff $diff $diffPath

    $addedCount = (As-Array $diff.added).Count
    $removedCount = (As-Array $diff.removed).Count
    $changedCount = (As-Array $diff.changed).Count
    $hasChanges = ($addedCount + $removedCount + $changedCount) -gt 0

    if ($hasChanges) {
        $confirmed = Read-Confirmation "Apply this database update and build patch package?"
    } else {
        $confirmed = Read-Confirmation "No database changes found. Build patch package anyway?"
    }

    if (-not $confirmed) {
        Write-Host "Cancelled. Database was not changed and no package was built."
        return
    }

    if ($hasChanges) {
        Apply-CandidateDatabase ([string]$diff.meta.candidatePath)
    } else {
        Write-Host "Keeping current database."
    }

    Write-Host ""
    Write-Host "Running rule tests..."
    Invoke-Checked "powershell" @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $testScript)

    $packagePatchVersion = $PatchVersion
    if (-not $packagePatchVersion) { $packagePatchVersion = [string]$diff.meta.newBuild }
    $packagePatchVersion = ConvertTo-SafeNamePart $packagePatchVersion
    if (-not $packagePatchVersion) { throw "Unable to determine patch version for zip name." }

    Write-Host ""
    Write-Host ("Building Aslain package for patch {0}..." -f $packagePatchVersion)
    Invoke-Checked "powershell" @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $buildScript,
        "-ProjectRoot", $ProjectRoot,
        "-PatchVersion", $packagePatchVersion
    )

    $zipPath = Join-Path (Join-Path $ProjectRoot "dist") "14.3-helper_Aslain-patch$packagePatchVersion.zip"
    Write-Host ""
    Write-Host ("Done: {0}" -f $zipPath) -ForegroundColor Green
} catch {
    $exitCode = 1
    Write-Host ""
    Write-Host ("ERROR: {0}" -f $_.Exception.Message) -ForegroundColor Red
} finally {
    Pause-IfNeeded
    if ($exitCode -ne 0) { exit $exitCode }
}
