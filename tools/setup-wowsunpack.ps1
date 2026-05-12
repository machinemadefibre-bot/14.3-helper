param(
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$InstallRoot = "",
    [string]$RustRoot = "",
    [switch]$Force
)

$ErrorActionPreference = "Stop"

if (-not $InstallRoot) {
    $InstallRoot = Join-Path $ProjectRoot "tools\wowsunpack-git"
}
if (-not $RustRoot) {
    $RustRoot = Join-Path $ProjectRoot "tools\rust"
}

$cargoHome = Join-Path $RustRoot "cargo"
$rustupHome = Join-Path $RustRoot "rustup"
$cargo = Join-Path $cargoHome "bin\cargo.exe"
$wowsunpack = Join-Path $InstallRoot "bin\wowsunpack.exe"

if ((Test-Path $wowsunpack) -and -not $Force) {
    & $wowsunpack --version
    Write-Host "wowsunpack already installed at $wowsunpack"
    return
}

$env:CARGO_HOME = $cargoHome
$env:RUSTUP_HOME = $rustupHome
$env:PATH = (Join-Path $cargoHome "bin") + ";" + $env:PATH

if (-not (Test-Path $cargo)) {
    $rustupInit = Join-Path $RustRoot "rustup-init.exe"
    New-Item -ItemType Directory -Force -Path $RustRoot | Out-Null
    if (-not (Test-Path $rustupInit)) {
        throw "Rust is not installed under $RustRoot. Download rustup-init.exe to $rustupInit, then rerun this script."
    }
    & $rustupInit -y --no-modify-path --profile minimal
    if ($LASTEXITCODE -ne 0) {
        throw "rustup-init failed with exit code $LASTEXITCODE"
    }
}

& $cargo install --git https://github.com/landaire/wows-toolkit wowsunpack --locked --root $InstallRoot --force
if ($LASTEXITCODE -ne 0) {
    throw "cargo install wowsunpack failed with exit code $LASTEXITCODE"
}

& $wowsunpack --version
Write-Host "Installed wowsunpack at $wowsunpack"
