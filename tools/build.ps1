param(
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$ZipName = "",
    [string]$PatchVersion = ""
)

$ErrorActionPreference = "Stop"

$src = Join-Path $ProjectRoot "src"
$dist = Join-Path $ProjectRoot "dist"
$build = Join-Path $ProjectRoot "build\package"

if (-not $ZipName) {
    if ($PatchVersion) {
        $safePatchVersion = ([string]$PatchVersion).Trim() -replace '[^A-Za-z0-9._-]+', '_'
        if (-not $safePatchVersion) { throw "PatchVersion produced an empty zip suffix." }
        $ZipName = "14.3-helper_Aslain-patch$safePatchVersion.zip"
    } else {
        $ZipName = "14.3-helper_Aslain.zip"
    }
}
if (-not $ZipName.EndsWith(".zip", [System.StringComparison]::OrdinalIgnoreCase)) {
    $ZipName = "$ZipName.zip"
}
$zip = Join-Path $dist $ZipName

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
