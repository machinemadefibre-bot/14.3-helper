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
$battleElementsPath = Join-Path $target "gui\battle_elements.xml"

if (-not (Test-Path $target)) {
    New-Item -ItemType Directory -Path $target | Out-Null
}

Copy-Item -LiteralPath (Join-Path $source "PnFMods") -Destination $target -Recurse -Force
Copy-Item -LiteralPath (Join-Path $source "gui") -Destination $target -Recurse -Force
Copy-Item -LiteralPath (Join-Path $source "PnFModsLoader.py") -Destination $target -Force

if (Test-Path -LiteralPath $battleElementsPath) {
    [xml]$battleElements = Get-Content -LiteralPath $battleElementsPath -Raw
    $elementList = $battleElements.'battle_elements.xml'.elementList
    if ($null -eq $elementList) {
        throw "elementList was not found in $battleElementsPath"
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
