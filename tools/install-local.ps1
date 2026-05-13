param(
    [string]$GameDir = "S:\SteamLibrary\steamapps\common\World of Warships",
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $GameDir)) {
    throw "Game directory not found: $GameDir"
}

$binDir = Join-Path $GameDir "bin"
$latest = Get-ChildItem -Directory -LiteralPath $binDir |
    Where-Object { $_.Name -match '^\d+$' } |
    Sort-Object { [int64]$_.Name } -Descending |
    Select-Object -First 1

if (-not $latest) {
    throw "No numeric build directory found under $binDir"
}

$target = Join-Path $latest.FullName "res_mods"
$source = Join-Path $ProjectRoot "src\res_mods"

if (-not (Test-Path $target)) {
    New-Item -ItemType Directory -Path $target | Out-Null
}

Copy-Item -LiteralPath (Join-Path $source "PnFMods") -Destination $target -Recurse -Force
Copy-Item -LiteralPath (Join-Path $source "gui") -Destination $target -Recurse -Force
Copy-Item -LiteralPath (Join-Path $source "PnFModsLoader.py") -Destination $target -Force

Write-Host "Installed APOvermatchAssistant to $target"
Write-Host "Start the game once so ModsInstaller_4_3_1 can patch gui\battle_elements.xml."
