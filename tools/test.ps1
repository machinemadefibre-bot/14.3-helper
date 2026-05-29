param(
    [string]$Python = "",
    [switch]$SkipPython,
    [switch]$Build
)

$ErrorActionPreference = "Stop"

$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path
$pythonTests = Join-Path $ProjectRoot "tests\overmatch_python_module_tests.py"

function Find-Python {
    if ($Python) {
        return @((Resolve-Path -LiteralPath $Python).Path)
    }

    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if ($pythonCommand) {
        return @($pythonCommand.Source)
    }

    $pyCommand = Get-Command py -ErrorAction SilentlyContinue
    if ($pyCommand) {
        return @($pyCommand.Source, "-3")
    }

    return $null
}

function Find-Node {
    $bundledNode = Join-Path $ProjectRoot ".tools\node\node.exe"
    if (Test-Path -LiteralPath $bundledNode) {
        return $bundledNode
    }

    $nodeCommand = Get-Command node -ErrorAction SilentlyContinue
    if ($nodeCommand) {
        return $nodeCommand.Source
    }

    return $null
}

function Invoke-Checked {
    param(
        [string]$FilePath,
        [string[]]$Arguments
    )

    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed: $FilePath $($Arguments -join ' ')"
    }
}

function Assert-PathExists {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Required path is missing: $Path"
    }
}

function Assert-TextMatches {
    param(
        [string]$Path,
        [string]$Pattern,
        [string]$Description
    )

    $text = Get-Content -LiteralPath $Path -Raw
    if ($text -notmatch $Pattern) {
        throw "$Description was not found in $Path"
    }
    return $Matches
}

function Assert-TextContains {
    param(
        [string]$Path,
        [string]$Needle,
        [string]$Description
    )

    $text = Get-Content -LiteralPath $Path -Raw
    if (-not $text.Contains($Needle)) {
        throw "$Description was not found in $Path"
    }
}

function Test-ProjectInvariants {
    $requiredSourceFiles = @(
        "src\res_mods\PnFMods\APOvermatchAssistant\Main.py",
        "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_constants.py",
        "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_database.py",
        "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_logging.py",
        "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_payload.py",
        "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_rules.py",
        "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_utils.py",
        "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.py",
        "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json",
        "src\res_mods\gui\unbound2\PnFMods\APOvermatchAssistant.unbound",
        "src\res_mods\PnFMods\ModsInstaller_4_3_1\mods\APOvermatchAssistant.xml",
        "tools\ap-penetration.mjs",
        "tools\diagnose-ap-penetration.mjs"
    )

    foreach ($relativePath in $requiredSourceFiles) {
        Assert-PathExists (Join-Path $ProjectRoot $relativePath)
    }

    $constantsPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_constants.py"
    $installerPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\ModsInstaller_4_3_1\mods\APOvermatchAssistant.xml"
    $unboundPath = Join-Path $ProjectRoot "src\res_mods\gui\unbound2\PnFMods\APOvermatchAssistant.unbound"
    $dataPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"

    $constantMatches = Assert-TextMatches -Path $constantsPath -Pattern "MOD_VERSION\s*=\s*'([^']+)'" -Description "MOD_VERSION"
    $constantVersion = $constantMatches[1]

    [xml]$installerXml = Get-Content -LiteralPath $installerPath -Raw
    $installerVersion = $installerXml.code.check.version
    if ($constantVersion -ne $installerVersion) {
        throw "Version mismatch: overmatch_constants.py has $constantVersion but APOvermatchAssistant.xml has $installerVersion"
    }
    if ($installerXml.code.target_File.file -ne "gui/battle_elements.xml") {
        throw "APOvermatchAssistant.xml must patch gui/battle_elements.xml."
    }
    $battleElement = $installerXml.code.target_File.root_Node.find_Node.insert.element
    if ($battleElement.elementName -ne "OA_APOvermatchAssistant") {
        throw "APOvermatchAssistant.xml elementName must mount OA_APOvermatchAssistant."
    }
    if ($battleElement.name -ne "unbound2APOvermatchAssistant") {
        throw "APOvermatchAssistant.xml element name must be unbound2APOvermatchAssistant."
    }
    $insertPosition = $installerXml.code.target_File.root_Node.find_Node.insert.attrs.position
    if ($insertPosition.insert -ne "after_node" -or $insertPosition.value_1 -ne "MainHud") {
        throw "APOvermatchAssistant.xml should insert the UI element after MainHud."
    }
    if (Test-Path -LiteralPath (Join-Path $ProjectRoot "src\res_mods\gui\battle_elements.xml")) {
        throw "Source package must not include static gui\battle_elements.xml; ModsInstaller_4_3_1 should patch the live file."
    }

    $requiredUnboundPatterns = @(
        "BEGIN GENERATED ARMOR DB",
        "END GENERATED ARMOR DB",
        "OA_ARMOR_DB_BUILD",
        "\(def element OA_APOvermatchAssistant\(\)",
        "\(def element OA_AmmoPanel",
        "\(def element OA_RulePanel",
        "\(def element OA_MainBeltRow",
        "getFirstWatcher\(CC\.selfVehicle\)",
        "selfVehicleEntity \? selfVehicleEntity\.weaponController : null",
        "aimAssist\.distance",
        "targetBeltObliquityDeg",
        "mainBeltHeadingMaxDeg",
        "weaponSlotsCount == 0",
        "isDefenseMode \|\| \(isSlotActive && isSupportedAmmo\)",
        "cameraEntity\.camera\.altVision",
        "\(width = 230\)",
        "\(def element OA_Row\(_prefix:str, _text:str, _color:number\)",
        "\(def element OA_BeltRow\(_prefix:str, _labelText:str, _labelColor:number, _bowText:str, _bowColor:number, _sternText:str, _sternColor:number\)",
        "'DEF' : 'ATK'",
        "\(textColor = 0xFFFFFF\)\s*\r?\n\s*\(noTranslate = true\)\s*\r?\n\s*\(width = 42px\)",
        "\(left = 146px\)",
        "\(width = 66px\)"
    )

    foreach ($pattern in $requiredUnboundPatterns) {
        $null = Assert-TextMatches -Path $unboundPath -Pattern $pattern -Description "Required unbound pattern"
    }

    $unboundText = Get-Content -LiteralPath $unboundPath -Raw
    $db = Get-Content -LiteralPath $dataPath -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($unboundText -notmatch "OA_ARMOR_DB_BUILD\s+'([^']*)'") {
        throw "APOvermatchAssistant.unbound must expose OA_ARMOR_DB_BUILD."
    }
    if ([string]$db.meta.gameBuild -ne $Matches[1]) {
        throw "Unbound armor DB build $($Matches[1]) does not match JSON armor DB build $($db.meta.gameBuild). Run tools\generate-unbound-armor-db.mjs."
    }
    if ([int]$db.schema -lt 3) {
        throw "Armor database schema must include AP penetration fields."
    }
    $shipsWithMainGuns = @($db.ships.PSObject.Properties.Value | Where-Object { [double]($_.mainGunCaliberMm) -gt 0 })
    $shipsWithApTables = @($shipsWithMainGuns | Where-Object { $_.mainGunAp -and $_.mainGunAp.table -and $_.mainGunAp.table.Count -ge 7 })
    if ($shipsWithMainGuns.Count -gt 0 -and ($shipsWithApTables.Count / [double]$shipsWithMainGuns.Count) -lt 0.40) {
        throw "AP table coverage is unexpectedly low: $($shipsWithApTables.Count)/$($shipsWithMainGuns.Count)."
    }
    foreach ($ship in $shipsWithApTables | Select-Object -First 10) {
        $sample = $ship.mainGunAp.table[0]
        if ([double]$sample.verticalPenetrationMm -le 0 -or [double]$sample.velocityMps -le 0) {
            throw "Invalid AP penetration sample for $($ship.name)."
        }
    }
    $yamato = $db.ships.PSObject.Properties["PJSB018_Yamato_1944"].Value
    $yamatoMainBelt = $yamato.armor.mainBelt
    $yamatoMainBeltText = @($yamatoMainBelt.values) -join "/"
    if ($yamatoMainBeltText -ne "410") {
        throw "Yamato main belt extraction should use only the 410 mm primary belt, actual=$yamatoMainBeltText."
    }
    if ([bool]$yamatoMainBelt.inclinationDeg.estimated -or [bool]$yamatoMainBelt.headingAngleDeg.estimated) {
        throw "Yamato main belt extraction should have measured inclination and heading-angle ranges."
    }
    if ([double]$yamatoMainBelt.inclinationDeg.min -lt 15 -or [double]$yamatoMainBelt.inclinationDeg.max -gt 30) {
        throw "Yamato main belt inclination range is outside the expected geometry-derived range."
    }
    if ([double]$yamatoMainBelt.headingAngleDeg.max -lt 1 -or [double]$yamatoMainBelt.headingAngleDeg.max -gt 12) {
        throw "Yamato main belt heading-angle range is outside the expected geometry-derived range."
    }
    if ($unboundText -match '\$datahub\.getSingleComponent\(CC\.weaponController\)') {
        throw "APOvermatchAssistant.unbound should not depend on the global CC.weaponController component."
    }
    if ($unboundText -match "\(def element OA_TargetPanel\(") {
        throw "Unused legacy OA_TargetPanel should not be kept in APOvermatchAssistant.unbound."
    }
    if ($unboundText -match "'In '" -or $unboundText -match "'Out '") {
        throw "English rule-panel mode prefixes should be ATK/DEF, not In/Out."
    }

    $rulePanelContentWidth = 230 - 18
    $rowRightEdge = 44 + 168
    $beltRightEdge = 146 + 66
    if ($rowRightEdge -gt $rulePanelContentWidth -or $beltRightEdge -gt $rulePanelContentWidth) {
        throw "Rule-panel text columns exceed the available content width."
    }
}

function Test-ToolingInvariants {
    $generatorPath = Join-Path $ProjectRoot "tools\generate-armor-db.ps1"
    $updatePath = Join-Path $ProjectRoot "tools\update-armor-db.ps1"
    $updateAndBuildPath = Join-Path $ProjectRoot "tools\update-armor-db-and-build.ps1"
    $manualEditorPath = Join-Path $ProjectRoot "tools\manual-edit-armor-db.mjs"

    Assert-TextContains -Path $generatorPath -Needle '-replace "`0", ""' -Description "Realm NUL-byte cleanup"
    $null = Assert-TextMatches -Path $generatorPath -Pattern "\^\[A-Z0-9\._-\]\+\$" -Description "Realm safe-character validation"
    Assert-TextContains -Path $generatorPath -Needle 'Test-Path -LiteralPath $localBuildCandidate' -Description "LiteralPath check for local GameParams candidate"
    Assert-TextContains -Path $generatorPath -Needle 'Get-Command node -All' -Description "Node candidate enumeration"
    Assert-TextContains -Path $generatorPath -Needle 'Skipping Node fast generator:' -Description "Node fast-generator fallback"
    Assert-TextContains -Path $updatePath -Needle 'function Get-UsableNode' -Description "Node helper executable probe"
    Assert-TextContains -Path $updatePath -Needle 'AllowUnrefinedDatabase' -Description "Explicit unrefined diagnostic mode"
    Assert-TextContains -Path $updatePath -Needle 'Node.js is required for armor database normalization and geometry refinement.' -Description "Required Node guard"
    Assert-TextContains -Path $updatePath -Needle 'function Resolve-GeneratedGameParamsJson' -Description "Generated GameParams refinement lookup"
    Assert-PathExists $manualEditorPath
    Assert-TextContains -Path $updateAndBuildPath -Needle 'Manually edit armor database' -Description "Manual editor menu option"
    Assert-TextContains -Path $updateAndBuildPath -Needle 'Extract main belt geometry' -Description "Main belt extraction menu option"
    Assert-TextContains -Path $updateAndBuildPath -Needle 'Invoke-ManualEditor' -Description "Manual editor launcher"
    Assert-TextContains -Path $updateAndBuildPath -Needle 'Invoke-MainBeltExtraction' -Description "Main belt extraction launcher"
    Assert-TextContains -Path $updateAndBuildPath -Needle 'Invoke-UnboundArmorDbGeneration' -Description "Unbound database sync after updates"
    Assert-TextContains -Path (Join-Path $ProjectRoot "tools\build.ps1") -Needle 'generate-unbound-armor-db.mjs' -Description "Build syncs Unbound armor database"
    Assert-TextContains -Path $manualEditorPath -Needle 'Database updated. JSON and Python database are in sync.' -Description "Manual editor JSON/Python sync"
    Assert-TextContains -Path $manualEditorPath -Needle 'values in mm, separated by /' -Description "Manual editor slash-separated value prompt"
    Assert-TextContains -Path (Join-Path $ProjectRoot "tools\generate-armor-db-fast.mjs") -Needle 'mainGunAp' -Description "Fast generator extracts AP shell data"
    Assert-TextContains -Path (Join-Path $ProjectRoot "tools\generate-unbound-armor-db.mjs") -Needle 'apv:' -Description "Unbound database embeds AP penetration tables"
    Assert-TextContains -Path (Join-Path $ProjectRoot "tools\generate-unbound-armor-db.mjs") -Needle 'hmx:' -Description "Unbound database embeds main belt heading-angle ranges"
    Assert-TextContains -Path (Join-Path $ProjectRoot "tools\refine-side-from-geometry.mjs") -Needle 'main-belt-only' -Description "Geometry refiner supports main belt only extraction"

    $updateAndBuildText = Get-Content -LiteralPath $updateAndBuildPath -Raw
    if ($updateAndBuildText -match 'Added ships /|Removed ships /|Changed ships /') {
        throw "Console diff headings must stay English-only to avoid code-page mojibake."
    }
}

Push-Location $ProjectRoot
try {
    Test-ProjectInvariants
    Test-ToolingInvariants

    $nodeExe = Find-Node
    if (-not $nodeExe) {
        throw "Node.js was not found. Install Node.js or keep .tools\node\node.exe for AP penetration diagnostics."
    }
    Invoke-Checked -FilePath $nodeExe -Arguments @((Join-Path $ProjectRoot "tools\diagnose-ap-penetration.mjs"), "--self-test")

    if (-not $SkipPython) {
        $pythonArgs = @(Find-Python)
        if (-not $pythonArgs) {
            throw "Python was not found. Install Python or rerun with -SkipPython to run only PowerShell checks."
        }

        $pythonExe = $pythonArgs[0]
        $pythonExtraArgs = @()
        if ($pythonArgs.Count -gt 1) {
            $pythonExtraArgs = $pythonArgs[1..($pythonArgs.Count - 1)]
        }
        Invoke-Checked -FilePath $pythonExe -Arguments ($pythonExtraArgs + @($pythonTests))
    } else {
        Write-Host "Skipping Python unit tests."
    }

    & (Join-Path $ProjectRoot "tools\test-rule.ps1")

    if ($Build) {
        & (Join-Path $ProjectRoot "tools\build.ps1")

        $dataPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
        $db = Get-Content -LiteralPath $dataPath -Raw -Encoding UTF8 | ConvertFrom-Json
        $safePatchVersion = ([string]$db.meta.gameBuild).Trim() -replace '[^A-Za-z0-9._-]+', '_'
        $zip = Join-Path $ProjectRoot "dist\14.3-helper_Aslain-patch$safePatchVersion.zip"
        if (-not (Test-Path $zip)) {
            throw "Expected package was not built: $zip"
        }

        $zipEntries = @(tar -tf $zip | ForEach-Object { $_.Trim() })
        if ($LASTEXITCODE -ne 0) {
            throw "Unable to list package contents: $zip"
        }
        $requiredEntries = @(
            "res_mods/PnFMods/APOvermatchAssistant/Main.py",
            "res_mods/PnFMods/APOvermatchAssistant/overmatch_constants.py",
            "res_mods/PnFMods/APOvermatchAssistant/overmatch_database.py",
            "res_mods/PnFMods/APOvermatchAssistant/overmatch_logging.py",
            "res_mods/PnFMods/APOvermatchAssistant/overmatch_payload.py",
            "res_mods/PnFMods/APOvermatchAssistant/overmatch_rules.py",
            "res_mods/PnFMods/APOvermatchAssistant/overmatch_utils.py",
            "res_mods/gui/unbound2/PnFMods/APOvermatchAssistant.unbound",
            "res_mods/PnFMods/ModsInstaller_4_3_1/mods/APOvermatchAssistant.xml"
        )

        foreach ($entry in $requiredEntries) {
            if ($zipEntries -notcontains $entry) {
                throw "Package is missing required entry: $entry"
            }
        }

        foreach ($entry in $zipEntries) {
            if ($entry -and -not $entry.StartsWith("res_mods/")) {
                throw "Aslain Custom_mods package entry must start with res_mods/: $entry"
            }
            if ($entry -eq "res_mods/gui/battle_elements.xml") {
                throw "Package must not include static battle_elements.xml; ModsInstaller_4_3_1 should patch the current Aslain-generated file."
            }
            if ($entry -match "__pycache__/|\.py[co]$") {
                throw "Package contains Python cache output: $entry"
            }
        }
    }

    Write-Host "All requested tests passed."
}
finally {
    Pop-Location
}
