param(
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$ZipName = "",
    [string]$PatchVersion = "",
    [string]$AslainCustomModsDir = ""
)

$ErrorActionPreference = "Stop"

$src = Join-Path $ProjectRoot "src"
$dist = Join-Path $ProjectRoot "dist"
$buildRoot = Join-Path ([System.IO.Path]::GetTempPath()) "14.3-helper-build"
$build = Join-Path $buildRoot ("package_" + [System.Guid]::NewGuid().ToString("N"))

function ConvertTo-SafeNamePart {
    param([string]$Value)
    $safe = ([string]$Value).Trim() -replace '[^A-Za-z0-9._-]+', '_'
    return $safe.Trim("_")
}

function Get-DefaultPatchVersion {
    $targetVersion = Get-TargetGameVersion
    if ($targetVersion) { return $targetVersion }

    $dbPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
    if (-not (Test-Path -LiteralPath $dbPath)) { return "" }

    try {
        $db = Get-Content -LiteralPath $dbPath -Raw -Encoding UTF8 | ConvertFrom-Json
        if ($db.meta -and $db.meta.gameBuild) { return [string]$db.meta.gameBuild }
    } catch {
        return ""
    }

    return ""
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

function Read-PatchVersionOrDefault {
    param([string]$DefaultValue)

    if ($PatchVersion) { return $PatchVersion }
    if (-not [Console]::IsInputRedirected) {
        $promptDefault = if ($DefaultValue) { $DefaultValue } else { "no patch suffix" }
        $answer = (Read-Host "Patch version for zip suffix (Enter for $promptDefault)").Trim()
        if ($answer) { return $answer }
    }
    return $DefaultValue
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

function Get-UnboundDatabaseBuild {
    $unboundPath = Join-Path $ProjectRoot "src\res_mods\gui\unbound2\PnFMods\APOvermatchAssistant.unbound"
    if (-not (Test-Path -LiteralPath $unboundPath)) { return "" }
    $text = Get-Content -LiteralPath $unboundPath -Raw
    if ($text -match "OA_ARMOR_DB_BUILD\s+'([^']*)'") { return $Matches[1] }
    return ""
}

function Invoke-UnboundArmorDbGeneration {
    $dbBuild = Get-DefaultPatchVersion
    $unboundBuild = Get-UnboundDatabaseBuild
    if ($dbBuild -and $dbBuild -eq $unboundBuild) { return }

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

if (-not $ZipName) {
    $modVersionNamePart = ConvertTo-SafeNamePart (Get-ModVersionNamePart)
    $packageNamePrefix = if ($modVersionNamePart) { "14.3-helper_$modVersionNamePart" } else { "14.3-helper" }
    $resolvedPatchVersion = Read-PatchVersionOrDefault (Get-DefaultPatchVersion)
    if ($resolvedPatchVersion) {
        $safePatchVersion = ConvertTo-SafeNamePart $resolvedPatchVersion
        if (-not $safePatchVersion) { throw "PatchVersion produced an empty zip suffix." }
        $ZipName = "${packageNamePrefix}_Aslain-patch$safePatchVersion.zip"
    } else {
        $ZipName = "${packageNamePrefix}_Aslain.zip"
    }
}
if (-not $ZipName.EndsWith(".zip", [System.StringComparison]::OrdinalIgnoreCase)) {
    $ZipName = "$ZipName.zip"
}
$zip = Join-Path $dist $ZipName

if (-not (Test-Path $dist)) {
    New-Item -ItemType Directory -Path $dist | Out-Null
}
if (-not (Test-Path $buildRoot)) {
    New-Item -ItemType Directory -Path $buildRoot | Out-Null
}

Invoke-UnboundArmorDbGeneration

try {
    New-Item -ItemType Directory -Path $build | Out-Null

    Copy-Item -LiteralPath (Join-Path $src "res_mods") -Destination $build -Recurse

    Get-ChildItem -Path $build -Recurse -Force |
        Where-Object { $_.PSIsContainer -and $_.Name -eq "__pycache__" } |
        Remove-Item -Recurse -Force
    Get-ChildItem -Path $build -Recurse -Force |
        Where-Object { -not $_.PSIsContainer -and ($_.Extension -eq ".pyc" -or $_.Extension -eq ".pyo") } |
        Remove-Item -Force

    if (Test-Path $zip) {
        Remove-Item -LiteralPath $zip -Force
    }

    Compress-Archive -Path (Join-Path $build "res_mods") -DestinationPath $zip -Force

    Write-Host "Built $zip"

    if ($AslainCustomModsDir) {
        if (-not (Test-Path -LiteralPath $AslainCustomModsDir)) {
            New-Item -ItemType Directory -Path $AslainCustomModsDir | Out-Null
        }
        $customZip = Join-Path $AslainCustomModsDir ([System.IO.Path]::GetFileName($zip))
        Copy-Item -LiteralPath $zip -Destination $customZip -Force
        Write-Host "Copied Aslain Custom_mods package: $customZip"
    }
}
finally {
    if (Test-Path -LiteralPath $build) {
        Remove-Item -LiteralPath $build -Recurse -Force
    }
}
