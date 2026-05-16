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
        "src\res_mods\PnFMods\ModsInstaller_4_3_1\mods\APOvermatchAssistant.xml"
    )

    foreach ($relativePath in $requiredSourceFiles) {
        Assert-PathExists (Join-Path $ProjectRoot $relativePath)
    }

    $constantsPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\overmatch_constants.py"
    $installerPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\ModsInstaller_4_3_1\mods\APOvermatchAssistant.xml"
    $unboundPath = Join-Path $ProjectRoot "src\res_mods\gui\unbound2\PnFMods\APOvermatchAssistant.unbound"

    $constantMatches = Assert-TextMatches -Path $constantsPath -Pattern "MOD_VERSION\s*=\s*'([^']+)'" -Description "MOD_VERSION"
    $constantVersion = $constantMatches[1]

    [xml]$installerXml = Get-Content -LiteralPath $installerPath -Raw
    $installerVersion = $installerXml.code.check.version
    if ($constantVersion -ne $installerVersion) {
        throw "Version mismatch: overmatch_constants.py has $constantVersion but APOvermatchAssistant.xml has $installerVersion"
    }

    $requiredUnboundPatterns = @(
        "BEGIN GENERATED ARMOR DB",
        "END GENERATED ARMOR DB",
        "OA_ARMOR_DB_BUILD",
        "\(def element OA_AmmoPanel",
        "\(def element OA_RulePanel",
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

Push-Location $ProjectRoot
try {
    Test-ProjectInvariants

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

        $zip = Join-Path $ProjectRoot "dist\14.3-helper_Aslain.zip"
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
