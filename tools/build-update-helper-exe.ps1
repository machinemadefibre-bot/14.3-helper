param(
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path
)

$ErrorActionPreference = "Stop"

$source = Join-Path $ProjectRoot "tools\UpdateArmorDbAndBuild.cs"
$output = Join-Path $ProjectRoot "tools\update-armor-db-and-build.exe"
$cscCandidates = @(
    (Join-Path $env:WINDIR "Microsoft.NET\Framework64\v4.0.30319\csc.exe"),
    (Join-Path $env:WINDIR "Microsoft.NET\Framework\v4.0.30319\csc.exe")
)

$csc = $cscCandidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
if (-not $csc) {
    throw "Unable to find .NET Framework csc.exe."
}

& $csc /nologo /target:exe /platform:anycpu /optimize+ /out:$output $source
if ($LASTEXITCODE -ne 0) {
    throw "csc.exe failed with exit code $LASTEXITCODE"
}

Write-Host "Built $output"
