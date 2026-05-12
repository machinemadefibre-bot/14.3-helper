param(
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path
)

$ErrorActionPreference = "Stop"

$src = Join-Path $ProjectRoot "src"
$dist = Join-Path $ProjectRoot "dist"
$build = Join-Path $ProjectRoot "build\package"
$zip = Join-Path $dist "APOvermatchAssistant_Aslain.zip"

if (Test-Path $build) {
    Remove-Item -LiteralPath $build -Recurse -Force
}
if (-not (Test-Path $dist)) {
    New-Item -ItemType Directory -Path $dist | Out-Null
}
New-Item -ItemType Directory -Path $build | Out-Null

Copy-Item -LiteralPath (Join-Path $src "res_mods") -Destination $build -Recurse

if (Test-Path $zip) {
    Remove-Item -LiteralPath $zip -Force
}

Compress-Archive -Path (Join-Path $build "res_mods") -DestinationPath $zip -Force

Write-Host "Built $zip"
