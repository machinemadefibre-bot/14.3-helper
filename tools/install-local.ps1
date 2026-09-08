param(
    [string]$GameDir = "S:\SteamLibrary\steamapps\common\World of Warships",
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$BuildVersion = ""
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $GameDir)) {
    throw "Game directory not found: $GameDir"
}

$binDir = Join-Path $GameDir "bin"
$numericBuilds = Get-ChildItem -Directory -LiteralPath $binDir |
    Where-Object { $_.Name -match '^\d+$' }

if ($BuildVersion) {
    if ($BuildVersion -notmatch '^\d+$') {
        throw "BuildVersion must be numeric: $BuildVersion"
    }
    $latest = $numericBuilds | Where-Object { $_.Name -eq $BuildVersion } | Select-Object -First 1
} else {
    $latest = $numericBuilds |
        Sort-Object { [int64]$_.Name } -Descending |
        Select-Object -First 1
}

if (-not $latest) {
    if ($BuildVersion) {
        throw "Requested build directory not found under ${binDir}: $BuildVersion"
    }
    throw "No numeric build directory found under $binDir"
}

$target = Join-Path $latest.FullName "res_mods"
$source = Join-Path $ProjectRoot "src\res_mods"
$battleElementsPath = Join-Path $target "gui\battle_elements.xml"

if (-not (Test-Path $target)) {
    New-Item -ItemType Directory -Path $target | Out-Null
}

Copy-Item -LiteralPath (Join-Path $source "PnFMods") -Destination $target -Recurse -Force
$guiTarget = Join-Path $target "gui"
$unboundTarget = Join-Path $guiTarget "unbound2"
$pnfUnboundTarget = Join-Path $unboundTarget "PnFMods"
$modsUnboundTarget = Join-Path $unboundTarget "mods"
New-Item -ItemType Directory -Force -Path $pnfUnboundTarget,$modsUnboundTarget | Out-Null
Copy-Item -LiteralPath (Join-Path $source "gui\unbound2\PnFMods\APOvermatchAssistant.unbound") -Destination $pnfUnboundTarget -Force
Copy-Item -LiteralPath (Join-Path $source "gui\unbound2\mods\draggable.unbound") -Destination $modsUnboundTarget -Force

$legacyTtaroPaths = @(
    (Join-Path $target "PnFMods\ModsInstaller_4_3_1\mods\TTaroModConfig.xml"),
    (Join-Path $pnfUnboundTarget "TTaroModConfig.unbound"),
    (Join-Path $pnfUnboundTarget "TTaroModConfigConstants.unbound"),
    (Join-Path $pnfUnboundTarget "TTaroModConfigTranslations.unbound")
)
foreach ($legacyTtaroPath in $legacyTtaroPaths) {
    if (Test-Path -LiteralPath $legacyTtaroPath) {
        Remove-Item -LiteralPath $legacyTtaroPath -Force
    }
}
Copy-Item -LiteralPath (Join-Path $source "PnFModsLoader.py") -Destination $target -Force

if (Test-Path -LiteralPath $battleElementsPath) {
    [xml]$battleElements = Get-Content -LiteralPath $battleElementsPath -Raw
    $elementList = $battleElements.'battle_elements.xml'.elementList
    if ($null -eq $elementList) {
        throw "elementList was not found in $battleElementsPath"
    }

    $legacyTtaroElements = @($elementList.element |
        Where-Object { $_.name -eq "unbound2TTaroModConfig" -or $_.elementName -eq "TTaroModConfig" })
    if ($legacyTtaroElements.Count -gt 0) {
        $legacyBackupPath = $battleElementsPath + ".before-remove-TTaro-" + (Get-Date -Format "yyyyMMddHHmmss") + ".bak"
        Copy-Item -LiteralPath $battleElementsPath -Destination $legacyBackupPath -Force
        foreach ($legacyTtaroElement in $legacyTtaroElements) {
            [void]$elementList.RemoveChild($legacyTtaroElement)
        }

        $legacySettings = New-Object System.Xml.XmlWriterSettings
        $legacySettings.Indent = $true
        $legacySettings.Encoding = New-Object System.Text.UTF8Encoding($false)
        $legacyWriter = [System.Xml.XmlWriter]::Create($battleElementsPath, $legacySettings)
        try {
            $battleElements.Save($legacyWriter)
        } finally {
            $legacyWriter.Close()
        }
        Write-Host "Removed legacy TTaro battle UI entries: $battleElementsPath"
        Write-Host "Backup: $legacyBackupPath"
    }

    $existing = $elementList.element |
        Where-Object { $_.name -eq "unbound2APOvermatchAssistant" } |
        Select-Object -First 1

    if (-not $existing) {
        $mainHud = $elementList.element |
            Where-Object { $_.elementName -eq "MainHud" } |
            Select-Object -First 1
        if (-not $mainHud) {
            throw "MainHud element was not found in $battleElementsPath"
        }

        $backupPath = $battleElementsPath + ".before-APOvermatchAssistant-" + (Get-Date -Format "yyyyMMddHHmmss") + ".bak"
        Copy-Item -LiteralPath $battleElementsPath -Destination $backupPath -Force

        $newElement = $battleElements.CreateElement("element")
        $newElement.SetAttribute("class", "lesta.unbound2.UbElement")
        $newElement.SetAttribute("elementName", "OA_APOvermatchAssistant")
        $newElement.SetAttribute("name", "unbound2APOvermatchAssistant")

        $properties = $battleElements.CreateElement("properties")
        $properties.SetAttribute("hitTest", "true")
        [void]$newElement.AppendChild($properties)
        [void]$elementList.InsertAfter($newElement, $mainHud)

        $settings = New-Object System.Xml.XmlWriterSettings
        $settings.Indent = $true
        $settings.Encoding = New-Object System.Text.UTF8Encoding($false)
        $writer = [System.Xml.XmlWriter]::Create($battleElementsPath, $settings)
        try {
            $battleElements.Save($writer)
        } finally {
            $writer.Close()
        }

        Write-Host "Patched battle UI entry: $battleElementsPath"
        Write-Host "Backup: $backupPath"
    } else {
        Write-Host "Battle UI entry already exists: $battleElementsPath"
    }
} else {
    Write-Host "battle_elements.xml not found; ModsInstaller_4_3_1 will patch it when the game starts: $battleElementsPath"
}

Write-Host "Installed APOvermatchAssistant to $target"
