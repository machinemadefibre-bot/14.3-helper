param(
    [string]$GameDir = "S:\SteamLibrary\steamapps\common\World of Warships",
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$WowsUnpack = "",
    [string]$GameParamsJson = "",
    [string]$Realm = "",
    [string]$ShipKeyFilter = "",
    [string]$GeometryDir = "",
    [int]$MaxShips = 0,
    [switch]$ExtractGameParams,
    [switch]$SkipGeometryRefine,
    [switch]$AllowUnrefinedDatabase,
    [switch]$Apply
)

$ErrorActionPreference = "Stop"

function Read-JsonFile {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return $null }
    return Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json
}

function Get-MetaValue {
    param($Database, [string]$Name)
    if ($null -eq $Database -or $null -eq $Database.meta) { return "" }
    $prop = $Database.meta.PSObject.Properties[$Name]
    if ($prop) { return [string]$prop.Value }
    return ""
}

function Get-ShipProperties {
    param($Database)
    if ($null -eq $Database -or $null -eq $Database.ships) { return @() }
    return @($Database.ships.PSObject.Properties)
}

function Join-Values {
    param($Value)
    if ($null -eq $Value) { return "" }
    if ($Value -is [System.Array]) {
        return (@($Value) | ForEach-Object { [string]$_ } | Sort-Object -Unique) -join ","
    }
    return [string]$Value
}

function Ship-Summary {
    param($Ship)
    if ($null -eq $Ship) { return [ordered]@{} }
    $armor = $Ship.armor
    $bowStern = if ($armor) { $armor.bowStern } else { $null }
    $belt = if ($armor) { $armor.extendedBowSternBelt } else { $null }
    return [ordered]@{
        name = [string]$Ship.name
        mainGunCaliberMm = [string]$Ship.mainGunCaliberMm
        mainGunHePenMm = [string]$Ship.mainGunHePenMm
        mainGunSapPenMm = [string]$Ship.mainGunSapPenMm
        bow = Join-Values $bowStern.bow
        stern = Join-Values $bowStern.stern
        deck = Join-Values $armor.deck.values
        side = Join-Values $armor.side.values
        beltPresent = [string]([bool]$belt.present)
        belt = Join-Values $belt.values
        bowBelt = Join-Values $belt.bow
        sternBelt = Join-Values $belt.stern
    }
}

function Compare-Ship {
    param([string]$Key, $OldShip, $NewShip)
    $oldSummary = Ship-Summary $OldShip
    $newSummary = Ship-Summary $NewShip
    $fields = New-Object System.Collections.ArrayList

    foreach ($field in $newSummary.Keys) {
        $oldValue = if ($oldSummary.Contains($field)) { $oldSummary[$field] } else { "" }
        $newValue = $newSummary[$field]
        if ($oldValue -ne $newValue) {
            [void]$fields.Add([ordered]@{
                field = $field
                old = $oldValue
                new = $newValue
            })
        }
    }

    if ($fields.Count -eq 0) { return $null }
    return [ordered]@{
        key = $Key
        name = $newSummary.name
        fields = @($fields)
    }
}

function Get-ShipByKey {
    param($Database, [string]$Key)
    if ($null -eq $Database -or $null -eq $Database.ships) { return $null }
    $prop = $Database.ships.PSObject.Properties[$Key]
    if ($prop) { return $prop.Value }
    return $null
}

function Write-MarkdownReport {
    param($Diff, [string]$Path)
    $lines = New-Object System.Collections.ArrayList
    [void]$lines.Add("# AP Overmatch Armor DB Diff")
    [void]$lines.Add("")
    [void]$lines.Add("- Old build: $($Diff.meta.oldBuild)")
    [void]$lines.Add("- New build: $($Diff.meta.newBuild)")
    [void]$lines.Add("- Old ships: $($Diff.meta.oldShipCount)")
    [void]$lines.Add("- New ships: $($Diff.meta.newShipCount)")
    [void]$lines.Add("- Added: $($Diff.added.Count)")
    [void]$lines.Add("- Removed: $($Diff.removed.Count)")
    [void]$lines.Add("- Changed: $($Diff.changed.Count)")
    [void]$lines.Add("")

    if ($Diff.added.Count -gt 0) {
        [void]$lines.Add("## Added Ships")
        [void]$lines.Add("")
        foreach ($ship in $Diff.added) {
            [void]$lines.Add("- $($ship.key) | $($ship.name) | caliber $($ship.mainGunCaliberMm)")
        }
        [void]$lines.Add("")
    }

    if ($Diff.removed.Count -gt 0) {
        [void]$lines.Add("## Removed Ships")
        [void]$lines.Add("")
        foreach ($ship in $Diff.removed) {
            [void]$lines.Add("- $($ship.key) | $($ship.name) | caliber $($ship.mainGunCaliberMm)")
        }
        [void]$lines.Add("")
    }

    if ($Diff.changed.Count -gt 0) {
        [void]$lines.Add("## Changed Ships")
        [void]$lines.Add("")
        [void]$lines.Add("| Ship | Field | Old | New |")
        [void]$lines.Add("| --- | --- | --- | --- |")
        foreach ($ship in $Diff.changed) {
            foreach ($field in $ship.fields) {
                $oldText = ([string]$field.old).Replace("|", "\|")
                $newText = ([string]$field.new).Replace("|", "\|")
                [void]$lines.Add("| $($ship.key) | $($field.field) | $oldText | $newText |")
            }
        }
        [void]$lines.Add("")
    }

    [System.IO.File]::WriteAllLines($Path, $lines, [System.Text.Encoding]::UTF8)
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

    if ($candidatePaths.Count -gt 0) {
        Write-Host "Skipping Node helper scripts: node is unavailable."
    }

    return ""
}

function Resolve-GeneratedGameParamsJson {
    param($Database, [string]$ProjectRoot)

    $build = Get-MetaValue $Database "gameBuild"
    $realm = Get-MetaValue $Database "realm"
    $candidatePaths = @()
    if ($build -and $realm) {
        $candidatePaths += Join-Path $ProjectRoot "build\gameparams\GameParams_$($build)_$($realm).json"
    }
    if ($realm) {
        $candidatePaths += Join-Path $ProjectRoot "build\gameparams\GameParams_$($realm).json"
        $candidatePaths += "C:\tmp\GameParams_$($realm).json"
    }

    foreach ($path in $candidatePaths) {
        if ($path -and (Test-Path -LiteralPath $path)) { return $path }
    }

    return ""
}

$dataPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
$updateDir = Join-Path $ProjectRoot "build\armor-update"
$snapshotDir = Join-Path $ProjectRoot "tools\armor_snapshots"
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$candidatePath = Join-Path $updateDir "armor_overmatch.candidate.$timestamp.json"
$diffJsonPath = Join-Path $updateDir "armor_diff.$timestamp.json"
$diffMdPath = Join-Path $updateDir "armor_diff.$timestamp.md"

New-Item -ItemType Directory -Force -Path $updateDir | Out-Null
New-Item -ItemType Directory -Force -Path $snapshotDir | Out-Null

$node = Get-UsableNode
if (-not $node -and -not $AllowUnrefinedDatabase) {
    throw "Node.js is required for armor database normalization and geometry refinement. Install Node.js or rerun with -AllowUnrefinedDatabase only for diagnostics."
}

$generateArgs = @(
    "-ExecutionPolicy", "Bypass",
    "-File", (Join-Path $PSScriptRoot "generate-armor-db.ps1"),
    "-GameDir", $GameDir,
    "-ProjectRoot", $ProjectRoot,
    "-OutPath", $candidatePath
)
if ($WowsUnpack) { $generateArgs += @("-WowsUnpack", $WowsUnpack) }
if ($GameParamsJson) { $generateArgs += @("-GameParamsJson", $GameParamsJson) }
if ($Realm) { $generateArgs += @("-Realm", $Realm) }
if ($ShipKeyFilter) { $generateArgs += @("-ShipKeyFilter", $ShipKeyFilter) }
if ($MaxShips -gt 0) { $generateArgs += @("-MaxShips", $MaxShips) }
if ($ExtractGameParams) { $generateArgs += "-ExtractGameParams" }

Write-Host "Generating candidate armor database..."
& powershell @generateArgs
if ($LASTEXITCODE -ne 0) {
    throw "generate-armor-db.ps1 failed with exit code $LASTEXITCODE"
}

$normalizeScript = Join-Path $PSScriptRoot "normalize-deck-values.mjs"
if ($node -and (Test-Path -LiteralPath $normalizeScript)) {
    Write-Host "Normalizing representative armor values..."
    & $node $normalizeScript $candidatePath
    if ($LASTEXITCODE -ne 0) {
        throw "normalize-deck-values.mjs failed with exit code $LASTEXITCODE"
    }
} else {
    Write-Host "Skipping representative armor normalization; unrefined diagnostic mode is enabled."
}

$refineScript = Join-Path $PSScriptRoot "refine-side-from-geometry.mjs"
if (-not $GeometryDir) {
    $GeometryDir = Join-Path $ProjectRoot "build\scratch\ship_geometry_flat"
}
$refineGameParamsJson = $GameParamsJson
if (-not $refineGameParamsJson) {
    $generatedDbForRefine = Read-JsonFile $candidatePath
    if ($generatedDbForRefine) {
        $refineGameParamsJson = Resolve-GeneratedGameParamsJson $generatedDbForRefine $ProjectRoot
    }
}
if (-not $SkipGeometryRefine -and $node -and $refineGameParamsJson -and (Test-Path -LiteralPath $refineScript) -and (Test-Path -LiteralPath $refineGameParamsJson) -and (Test-Path -LiteralPath $GeometryDir)) {
    Write-Host "Refining armor values from geometry positions..."
    & $node $refineScript --db $candidatePath --game-params $refineGameParamsJson --geometry-dir $GeometryDir
    if ($LASTEXITCODE -ne 0) {
        throw "refine-side-from-geometry.mjs failed with exit code $LASTEXITCODE"
    }
} else {
    if (-not $SkipGeometryRefine -and -not $AllowUnrefinedDatabase) {
        throw "Geometry refinement could not run. Provide -GameParamsJson and -GeometryDir, or rerun with -AllowUnrefinedDatabase only for diagnostics."
    }
    Write-Host "Skipping geometry refinement; unrefined diagnostic mode is enabled or -SkipGeometryRefine was specified."
}

$oldDb = Read-JsonFile $dataPath
$newDb = Read-JsonFile $candidatePath
if ($null -eq $newDb) { throw "Candidate database was not created: $candidatePath" }

$oldProps = Get-ShipProperties $oldDb
$newProps = Get-ShipProperties $newDb
$oldKeys = @($oldProps | ForEach-Object { $_.Name })
$newKeys = @($newProps | ForEach-Object { $_.Name })
$oldKeySet = @{}
$newKeySet = @{}
foreach ($key in $oldKeys) { $oldKeySet[$key] = $true }
foreach ($key in $newKeys) { $newKeySet[$key] = $true }

$added = New-Object System.Collections.ArrayList
$removed = New-Object System.Collections.ArrayList
$changed = New-Object System.Collections.ArrayList

foreach ($key in $newKeys) {
    $newShip = Get-ShipByKey $newDb $key
    if (-not $oldKeySet.ContainsKey($key)) {
        $summary = Ship-Summary $newShip
        [void]$added.Add([ordered]@{
            key = $key
            name = $summary.name
            mainGunCaliberMm = $summary.mainGunCaliberMm
        })
        continue
    }
    $oldShip = Get-ShipByKey $oldDb $key
    $shipDiff = Compare-Ship $key $oldShip $newShip
    if ($shipDiff) { [void]$changed.Add($shipDiff) }
}

foreach ($key in $oldKeys) {
    if ($newKeySet.ContainsKey($key)) { continue }
    $oldShip = Get-ShipByKey $oldDb $key
    $summary = Ship-Summary $oldShip
    [void]$removed.Add([ordered]@{
        key = $key
        name = $summary.name
        mainGunCaliberMm = $summary.mainGunCaliberMm
    })
}

$diff = [ordered]@{
    meta = [ordered]@{
        generatedAt = (Get-Date).ToString("s")
        oldBuild = Get-MetaValue $oldDb "gameBuild"
        newBuild = Get-MetaValue $newDb "gameBuild"
        oldRealm = Get-MetaValue $oldDb "realm"
        newRealm = Get-MetaValue $newDb "realm"
        oldShipCount = $oldKeys.Count
        newShipCount = $newKeys.Count
        candidatePath = $candidatePath
    }
    added = @($added)
    removed = @($removed)
    changed = @($changed)
}

($diff | ConvertTo-Json -Depth 20) | Set-Content -LiteralPath $diffJsonPath -Encoding UTF8
Write-MarkdownReport $diff $diffMdPath

Write-Host "Diff written:"
Write-Host "  $diffJsonPath"
Write-Host "  $diffMdPath"
Write-Host "Summary: added=$($added.Count), removed=$($removed.Count), changed=$($changed.Count)"

if ($Apply) {
    if (Test-Path -LiteralPath $dataPath) {
        $oldBuild = Get-MetaValue $oldDb "gameBuild"
        if (-not $oldBuild) { $oldBuild = "unknown-build" }
        $backupPath = Join-Path $snapshotDir "armor_overmatch.$oldBuild.$timestamp.json"
        Copy-Item -LiteralPath $dataPath -Destination $backupPath -Force
        Write-Host "Backed up old database to $backupPath"
    }
    Copy-Item -LiteralPath $candidatePath -Destination $dataPath -Force
    $candidatePyPath = [System.IO.Path]::ChangeExtension($candidatePath, ".py")
    $dataPyPath = [System.IO.Path]::ChangeExtension($dataPath, ".py")
    if (Test-Path -LiteralPath $candidatePyPath) {
        Copy-Item -LiteralPath $candidatePyPath -Destination $dataPyPath -Force
    }
    Write-Host "Applied candidate database to $dataPath"
} else {
    Write-Host "Report-only mode. Rerun with -Apply to replace the committed database."
}
