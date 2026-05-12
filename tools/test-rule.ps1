param(
    [string]$CasesPath = "$PSScriptRoot\..\tests\overmatch_cases.json"
)

$ErrorActionPreference = "Stop"

function Get-OvermatchState {
    param(
        [double]$Caliber,
        [double[]]$Armor
    )

    if ($null -eq $Armor -or $Armor.Count -eq 0) {
        return "unknown"
    }

    $limit = $Caliber / 14.3
    $hits = @($Armor | ForEach-Object { $limit -ge [double]$_ })

    if (($hits | Where-Object { $_ -eq $false }).Count -eq 0) {
        return "yes"
    }
    if (($hits | Where-Object { $_ -eq $true }).Count -gt 0) {
        return "partial"
    }
    return "no"
}

function Get-PenetrationState {
    param(
        [double]$Penetration,
        [double[]]$Armor
    )

    if ($null -eq $Armor -or $Armor.Count -eq 0) {
        return "unknown"
    }

    $hits = @($Armor | ForEach-Object { $Penetration -ge [double]$_ })

    if (($hits | Where-Object { $_ -eq $false }).Count -eq 0) {
        return "yes"
    }
    if (($hits | Where-Object { $_ -eq $true }).Count -gt 0) {
        return "partial"
    }
    return "no"
}

$cases = Get-Content -LiteralPath $CasesPath -Raw | ConvertFrom-Json
$failed = 0

foreach ($case in $cases) {
    $armor = @($case.armor)
    $actual = Get-OvermatchState -Caliber ([double]$case.caliber) -Armor $armor
    if ($actual -ne $case.expected) {
        Write-Host "FAIL caliber=$($case.caliber) armor=$($armor -join '/') expected=$($case.expected) actual=$actual"
        $failed++
    }
}

$penetrationCases = @(
    @{ penetration = 34; armor = @(32); expected = "yes" },
    @{ penetration = 34; armor = @(38); expected = "no" },
    @{ penetration = 34; armor = @(32, 38); expected = "partial" },
    @{ penetration = 68; armor = @(32, 38); expected = "yes" },
    @{ penetration = 36; armor = @(40); expected = "no" }
)

foreach ($case in $penetrationCases) {
    $armor = @($case.armor)
    $actual = Get-PenetrationState -Penetration ([double]$case.penetration) -Armor $armor
    if ($actual -ne $case.expected) {
        Write-Host "FAIL penetration=$($case.penetration) armor=$($armor -join '/') expected=$($case.expected) actual=$actual"
        $failed++
    }
}

$dataPath = Join-Path $PSScriptRoot "..\src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
if (Test-Path $dataPath) {
    $db = Get-Content -LiteralPath $dataPath -Raw | ConvertFrom-Json
    $hindenburg = $db.ships.PSObject.Properties["PGSC110_Hindenburg"].Value
    $deck = @($hindenburg.armor.deck.values)
    $deckText = $deck -join "/"
    if ($deckText -ne "30") {
        Write-Host "FAIL PGSC110_Hindenburg deck expected=30 actual=$deckText"
        $failed++
    }
    $mecklenburgApVsHindenburgDeck = Get-OvermatchState -Caliber 305 -Armor ([double[]]$deck)
    if ($mecklenburgApVsHindenburgDeck -ne "no") {
        Write-Host "FAIL Mecklenburg AP vs Hindenburg deck expected=no actual=$mecklenburgApVsHindenburgDeck"
        $failed++
    }

    $prinzHeinrich = $db.ships.PSObject.Properties["PGSB207_Prinz_Heinrich"].Value
    $prinzHeinrichSide = @($prinzHeinrich.armor.side.values)
    $prinzHeinrichSideText = $prinzHeinrichSide -join "/"
    if ($prinzHeinrichSideText -ne "150") {
        Write-Host "FAIL PGSB207_Prinz_Heinrich side expected=150 actual=$prinzHeinrichSideText"
        $failed++
    }

    $azurPrinzHeinrich = $db.ships.PSObject.Properties["PGSB517_AZUR_Prinz_Heinrich"].Value
    $azurSide = @($azurPrinzHeinrich.armor.side.values)
    $azurSideText = $azurSide -join "/"
    if ($azurSideText -ne "150") {
        Write-Host "FAIL PGSB517_AZUR_Prinz_Heinrich side expected=150 actual=$azurSideText"
        $failed++
    }

    $bismarckSideKeys = @(
        "PGSB108_Bismarck",
        "PGSB598_Black_Tirpitz",
        "PGSB708_Bismarck_1941",
        "PGSB818_BA_Tirpitz",
        "PGSB898_Azur_Bismarck",
        "PXSB005_Bismarck_H2017"
    )
    foreach ($shipKey in $bismarckSideKeys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        $side = @($ship.armor.side.values)
        $sideText = $side -join "/"
        if ($sideText -ne "160") {
            Write-Host "FAIL $shipKey side expected=160 actual=$sideText"
            $failed++
        }
    }

    $shimakazeGunKeys = @(
        "PJSD012_Shimakaze_1943",
        "PJSD890_AZUR_Shimakaze",
        "PJSD912_Shimakaze_1943",
        "PXSD012_Shimakaze2",
        "PXSD016_Shimakaze_PA",
        "PXSD022_Shimakaze_H2019"
    )
    foreach ($shipKey in $shimakazeGunKeys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        if ([int]$ship.mainGunCaliberMm -ne 127) {
            Write-Host "FAIL $shipKey caliber expected=127 actual=$($ship.mainGunCaliberMm)"
            $failed++
        }
        if ([int]$ship.mainGunHePenMm -ne 21) {
            Write-Host "FAIL $shipKey HE pen expected=21 actual=$($ship.mainGunHePenMm)"
            $failed++
        }
    }

    $noExtendedBeltKeys = @(
        "PJSC520_Yoshino",
        "PJSC590_Black_Yoshino",
        "PXSB054_Yoshino_modern",
        "PJSC510_Azumaya",
        "PJSC519_AZUR_Azuma",
        "PJSC829_Black_Azumaya",
        "PRSC509_Kronshtadt"
    )
    foreach ($shipKey in $noExtendedBeltKeys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        if ([bool]$ship.armor.extendedBowSternBelt.present) {
            $values = @($ship.armor.extendedBowSternBelt.values) -join "/"
            Write-Host "FAIL $shipKey extended belt expected=false actual=true values=$values"
            $failed++
        }
    }

    $extendedBeltKeys = @(
        "PRSC520_Stalingrad",
        "PRSC310_Petropavlovsk",
        "PHSC509_Van_Speijk"
    )
    foreach ($shipKey in $extendedBeltKeys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        if (-not [bool]$ship.armor.extendedBowSternBelt.present) {
            Write-Host "FAIL $shipKey extended belt expected=true actual=false"
            $failed++
        }
    }
}

if ($failed -gt 0) {
    throw "$failed rule case(s) failed."
}

Write-Host "All overmatch and penetration rule cases passed."
