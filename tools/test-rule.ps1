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

    $geometrySideExpectations = [ordered]@{
        "PGSC110_Hindenburg" = "30"
        "PISC510_Napoli" = "60"
        "PISC590_Black_Napoli" = "60"
        "PASC510_Alaska" = "28"
        "PASB017_Montana_1945" = "38"
        "PASB012_North_Carolina_1945" = "32"
        "PJSB018_Yamato_1944" = "32"
        "PJSB021_Izumo_1938" = "32"
        "PGSB109_Friedrich_der_Grosse" = "145/235"
        "PBSB210_St_Vincent" = "32"
        "PISC507_Duca_degli_Abruzzi" = "20/30"
        "PISC719_Ferrante_Gonzaga" = "16/30"
        "PVSC106_Almirante_Cochrane" = "20/30"
        "PGSB205_Derfflinger" = "150/235/265/270"
    }
    foreach ($shipKey in $geometrySideExpectations.Keys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        $side = @($ship.armor.side.values)
        $sideText = $side -join "/"
        if ($sideText -ne $geometrySideExpectations[$shipKey]) {
            Write-Host "FAIL $shipKey side expected=$($geometrySideExpectations[$shipKey]) actual=$sideText"
            $failed++
        }
    }

    $geometryDeckExpectations = [ordered]@{
        "PGSB109_Friedrich_der_Grosse" = "50/80"
        "PGSB509_Pommern" = "50/80"
        "PGSB599_Black_Pommern" = "50/80"
        "PBSB210_St_Vincent" = "40"
        "PBSB998_St_Lawrence" = "32"
        "PBSB209_Duncan" = "32"
        "PGSB205_Derfflinger" = "25/35"
        "PISC507_Duca_degli_Abruzzi" = "25"
        "PISC719_Ferrante_Gonzaga" = "16"
        "PVSC106_Almirante_Cochrane" = "25"
        "PGSC110_Hindenburg" = "30"
        "PASB017_Montana_1945" = "38"
        "PJSB018_Yamato_1944" = "57"
        "PJSB021_Izumo_1938" = "57"
    }
    foreach ($shipKey in $geometryDeckExpectations.Keys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        $deckText = @($ship.armor.deck.values) -join "/"
        if ($deckText -ne $geometryDeckExpectations[$shipKey]) {
            Write-Host "FAIL $shipKey deck expected=$($geometryDeckExpectations[$shipKey]) actual=$deckText"
            $failed++
        }
    }

    $carrierGeometryExpectations = [ordered]@{
        "PASA510_Roosevelt" = @{ deck = "87"; side = "19" }
        "PGSA110_Manfred_Richthofen" = @{ deck = "50"; side = "145/150" }
        "PJSA110_Hakuryu" = @{ deck = "95"; side = "19" }
        "PJSA710_Shinano" = @{ deck = "75"; side = "30" }
        "PRSA110_Admiral_Nakhimov" = @{ deck = "50"; side = "25" }
    }
    foreach ($shipKey in $carrierGeometryExpectations.Keys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        $expected = $carrierGeometryExpectations[$shipKey]
        $deckText = @($ship.armor.deck.values) -join "/"
        $sideText = @($ship.armor.side.values) -join "/"
        if ($deckText -ne $expected.deck) {
            Write-Host "FAIL $shipKey deck expected=$($expected.deck) actual=$deckText"
            $failed++
        }
        if ($sideText -ne $expected.side) {
            Write-Host "FAIL $shipKey side expected=$($expected.side) actual=$sideText"
            $failed++
        }
    }

    $submarineHullExpectations = [ordered]@{
        "PBSS910_Selkie" = "6/16/19/25"
        "PJSS508_I58" = "16/19/25"
        "PXSS207_Lazarus_Centurio" = "16/19/25"
        "PXSS307_Cyrus_Herrero" = "16/19/25"
        "PXSS407_Dr_Frankenship" = "13/16/19"
        "PXSS507_Klaus_V_Teslau" = "16/19/25"
    }
    foreach ($shipKey in $submarineHullExpectations.Keys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        $expected = $submarineHullExpectations[$shipKey]
        $bowText = @($ship.armor.bowStern.bow) -join "/"
        $sternText = @($ship.armor.bowStern.stern) -join "/"
        $deckText = @($ship.armor.deck.values) -join "/"
        $sideText = @($ship.armor.side.values) -join "/"
        if ($bowText -ne $expected -or $sternText -ne $expected -or $deckText -ne $expected -or $sideText -ne $expected) {
            Write-Host "FAIL $shipKey submarine hull expected=$expected actual=bow:$bowText stern:$sternText deck:$deckText side:$sideText"
            $failed++
        }
        if ([bool]$ship.armor.extendedBowSternBelt.present) {
            Write-Host "FAIL $shipKey submarine extended belt expected=false actual=true"
            $failed++
        }
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

    $hipperSideExpectations = [ordered]@{
        "PGSC108_Hipper" = "27"
        "PGSC508_Prinz_Eugen" = "27"
        "PGSC518_Mainz" = "25"
        "PGSC598_Black_Mainz" = "25"
        "PGSC729_Blucher" = "27"
    }
    foreach ($shipKey in $hipperSideExpectations.Keys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        $side = @($ship.armor.side.values)
        $sideText = $side -join "/"
        if ($sideText -ne $hipperSideExpectations[$shipKey]) {
            Write-Host "FAIL $shipKey side expected=$($hipperSideExpectations[$shipKey]) actual=$sideText"
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
        "PXSB054_Yoshino_modern"
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
        "PHSC509_Van_Speijk",
        "PGSC111_Clausewitz",
        "PGSC891_Clausewitz_PLUS"
    )
    foreach ($shipKey in $extendedBeltKeys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        if (-not [bool]$ship.armor.extendedBowSternBelt.present) {
            Write-Host "FAIL $shipKey extended belt expected=true actual=false"
            $failed++
        }
    }

    $extendedBeltValueCases = @{
        "PGSC110_Hindenburg" = "27/40/90"
        "PGSC111_Clausewitz" = "27/40/90"
        "PGSC891_Clausewitz_PLUS" = "27/40/90"
        "PBSB507_Hood" = "127/152"
        "PJSC510_Azumaya" = "25/120/175"
        "PJSC520_Yoshino" = "25/120/175"
        "PJSB021_Izumo_1938" = "305"
        "PZSB509_Izumo_Bajie" = "305"
        "PRSC509_Kronshtadt" = "25"
    }
    foreach ($shipKey in $extendedBeltValueCases.Keys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        $values = @($ship.armor.extendedBowSternBelt.values) -join "/"
        if ($values -ne $extendedBeltValueCases[$shipKey]) {
            Write-Host "FAIL $shipKey extended belt expected=$($extendedBeltValueCases[$shipKey]) actual=$values"
            $failed++
        }
    }

    $extendedBeltDirectionCases = @{
        "PGSC110_Hindenburg" = @{ bow = "27/40"; stern = "90" }
        "PGSC111_Clausewitz" = @{ bow = "27/40"; stern = "90" }
        "PGSC891_Clausewitz_PLUS" = @{ bow = "27/40"; stern = "90" }
        "PBSB507_Hood" = @{ bow = "127/152"; stern = "152" }
        "PJSC510_Azumaya" = @{ bow = "25"; stern = "25/120/175" }
        "PJSC520_Yoshino" = @{ bow = "25"; stern = "25/120/175" }
        "PJSB021_Izumo_1938" = @{ bow = ""; stern = "305" }
        "PZSB509_Izumo_Bajie" = @{ bow = ""; stern = "305" }
        "PRSC509_Kronshtadt" = @{ bow = "25"; stern = "" }
    }
    foreach ($shipKey in $extendedBeltDirectionCases.Keys) {
        $ship = $db.ships.PSObject.Properties[$shipKey].Value
        $belt = $ship.armor.extendedBowSternBelt
        $bow = @($belt.bow) -join "/"
        $stern = @($belt.stern) -join "/"
        $expected = $extendedBeltDirectionCases[$shipKey]
        if ($bow -ne $expected.bow -or $stern -ne $expected.stern) {
            Write-Host "FAIL $shipKey extended belt directions expected=bow:$($expected.bow),stern:$($expected.stern) actual=bow:$bow,stern:$stern"
            $failed++
        }
    }
}

if ($failed -gt 0) {
    throw "$failed rule case(s) failed."
}

Write-Host "All overmatch and penetration rule cases passed."
