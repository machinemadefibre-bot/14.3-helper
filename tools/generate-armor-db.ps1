param(
    [string]$GameDir = "S:\SteamLibrary\steamapps\common\World of Warships",
    [string]$WowsUnpack = "",
    [string]$ProjectRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$OverridePath = "$PSScriptRoot\armor_overmatch.overrides.json",
    [string]$GameParamsJson = "",
    [string]$OutPath = "",
    [string]$Realm = "",
    [string]$ShipKeyFilter = "",
    [switch]$ExtractGameParams,
    [int]$MaxShips = 0
)

$ErrorActionPreference = "Stop"

# Copied from wows-toolkit/wowsunpack's py_collisionMaterialName table.
# Armor keys are encoded as (model_index << 16) | material_id.
$CollisionMaterialNames = @(
    "common", "zero",
    "Dual_SSC_Bow_Side", "Dual_SSC_St_Side", "Dual_Cas_OCit_Belt", "Dual_OCit_St_Trans",
    "Dual_OCit_Bow_Trans", "Dual_Cit_Bow_Side", "Dual_Cit_Bow_Belt", "Dual_Cit_Bow_ArtSide",
    "Dual_Cit_St_Side", "Dual_Cit_St_Belt", "Bottom", "Dual_Cit_St_ArtSide",
    "Dual_Cas_Bow_Belt", "Dual_Cas_St_Belt", "Dual_Cas_SSC_Belt",
    "Dual_SSC_Bow_ConstrSide", "Dual_SSC_St_ConstrSide", "Cas_Inclin", "SSC_Inclin",
    "Dual_Cas_SSC_Inclin", "Dual_Cas_Bow_Inclin", "Dual_Cas_St_Inclin",
    "Dual_SSC_Bow_Inclin", "Dual_SSC_St_Inclin", "Dual_Cit_Bow_Bulge",
    "Dual_Cit_St_Bulge", "Dual_Cas_SS_Belt", "Dual_Cit_Cas_ArtDeck",
    "Dual_Cit_Cas_ArtSide", "Dual_OCit_OCit_Side",
    "TurretSide", "TurretTop", "TurretFront", "TurretAft", "FunnelSide", "ArtBottom",
    "ArtSide", "ArtTop", "AuTurretAft", "AuTurretBarbette", "AuTurretDown",
    "AuTurretFwd", "AuTurretSide", "AuTurretTop",
    "Bow_Belt", "Bow_Bottom", "Bow_ConstrSide", "Bow_Deck", "Bow_Inclin", "Bow_Trans",
    "BridgeBottom", "BridgeSide", "BridgeTop",
    "Cas_AftTrans", "Cas_Belt", "Cas_Deck", "Cas_FwdTrans",
    "Cit_AftTrans", "Cit_Barbette", "Cit_Belt", "Cit_Bottom", "Cit_Bulge", "Cit_Deck",
    "Cit_FwdTrans", "Cit_Inclin", "Cit_Side", "Dual_Cit_Cas_Bulge",
    "ConstrSide", "Dual_Cit_Cas_Belt", "Bow_Fdck", "St_Fdck", "KdpBottom", "KdpSide",
    "KdpTop", "OCit_AftTrans", "OCit_Belt", "OCit_Deck", "OCit_FwdTrans",
    "RudderAft", "RudderFwd", "RudderSide", "RudderTop",
    "SSC_AftTrans", "SSCasemate", "SSC_ConstrSide", "SSC_Deck", "SSC_FwdTrans",
    "SS_Side", "SS_Top",
    "St_Belt", "St_Bottom", "St_ConstrSide", "St_Deck", "St_Inclin", "St_Trans",
    "TurretBarbette", "TurretBarbette2", "TurretDown", "TurretFwd", "Bulge", "Trans",
    "Deck", "Belt", "Dual_Cit_SSC_Bulge", "Inclin",
    "SS_BridgeTop", "SS_BridgeSide", "SS_BridgeBottom", "Cas_Bottom",
    "SideCit", "DeckCit", "TransCit", "InclinCit", "SideCas", "DeckCas", "TransCas",
    "InclinCas", "SideSSC", "DeckSSC", "TransSSC", "InclinSSC", "SideBow", "DeckBow",
    "TransBow", "InclinBow", "SideStern", "DeckStern", "TransStern", "InclinStern",
    "SideSS", "DeckSS", "TransSS",
    "Tur1GkBar", "Tur2GkBar", "Tur3GkBar", "Tur4GkBar", "Tur5GkBar", "Tur6GkBar",
    "Tur7GkBar", "Tur8GkBar", "Tur9GkBar", "Tur10GkBar", "Tur11GkBar", "Tur12GkBar",
    "Tur13GkBar", "Tur14GkBar", "Tur15GkBar", "Tur16GkBar", "Tur17GkBar",
    "Tur18GkBar", "Tur19GkBar", "Tur20GkBar",
    "Dual_Cas_Bow_Trans", "Dual_Cas_Bow_Deck", "Dual_Cas_St_Trans", "Dual_Cas_St_Deck",
    "Dual_Cas_SSC_Deck", "Dual_Cas_SSC_Trans", "Dual_Cas_SS_Deck", "Dual_Cas_SS_Trans",
    "Dual_SSC_Bow_Trans", "Dual_SSC_Bow_Deck", "Dual_SSC_St_Trans", "Dual_SSC_St_Deck",
    "Dual_SSC_SS_Deck", "Dual_SSC_SS_Trans", "Dual_Bow_SS_Deck", "Dual_Bow_SS_Trans",
    "Dual_St_SS_Deck", "Dual_St_SS_Trans", "Dual_Cit_Bow_Bottom", "Dual_Cit_St_Bottom",
    "Tur1GkDown", "Tur2GkDown", "Tur3GkDown", "Tur4GkDown", "Tur5GkDown",
    "Tur6GkDown", "Tur7GkDown", "Tur8GkDown", "Tur9GkDown", "Tur10GkDown",
    "Tur11GkDown", "Tur12GkDown", "Tur13GkDown", "Tur14GkDown", "Tur15GkDown",
    "Tur16GkDown", "Tur17GkDown", "Tur18GkDown", "Tur19GkDown", "Tur20GkDown",
    "Dual_Cit_Cit_Deck", "Dual_Cit_Cit_Inclin", "Dual_Cit_Cit_Trans",
    "Dual_Cit_Cit_Side", "Dual_Cas_Cas_Belt", "Dual_Cas_Cas_Deck",
    "Dual_SSC_SSC_ConstrSide", "Dual_SSC_SSC_Deck", "Dual_Bow_Bow_Deck",
    "Dual_Bow_Bow_ConstrSide", "Dual_St_St_Deck", "Dual_St_St_ConstrSide",
    "Dual_SS_SS_Top", "Dual_SS_SS_Side", "Dual_Cit_Bow_ArtDeck",
    "Dual_Cit_St_ArtDeck", "Dual_Cas_Bow_Side", "Dual_Cas_St_Side",
    "Dual_Cit_Cas_Side", "Dual_Cit_SSC_Side",
    "Tur1GkTop", "Tur2GkTop", "Tur3GkTop", "Tur4GkTop", "Tur5GkTop", "Tur6GkTop",
    "Tur7GkTop", "Tur8GkTop", "Tur9GkTop", "Tur10GkTop", "Tur11GkTop", "Tur12GkTop",
    "Tur13GkTop", "Tur14GkTop", "Tur15GkTop", "Tur16GkTop", "Tur17GkTop",
    "Tur18GkTop", "Tur19GkTop", "Tur20GkTop",
    "Cas_Hang", "Cas_Fdck", "SSC_Fdck", "SSC_Hang", "SS_SGBarbette", "SS_SGDown",
    "SGBarbetteSS", "SGDownSS",
    "Dual_Cit_Cas_Deck", "Dual_Cit_Cas_Inclin", "Dual_Cit_Cas_Trans",
    "Dual_Cit_SSC_Deck", "Dual_Cit_SSC_Inclin", "Dual_Cit_SSC_Trans",
    "Dual_Cit_Bow_Trans", "Dual_Cit_Bow_Inclin", "Dual_Cit_Bow_Deck",
    "Dual_Cit_St_Trans", "Dual_Cit_St_Inclin", "Dual_Cit_St_Deck", "Dual_Cit_SS_Deck"
)

function Get-LatestBuildDir {
    param([string]$Root)
    $binDir = Join-Path $Root "bin"
    Get-ChildItem -Directory -LiteralPath $binDir |
        Where-Object { $_.Name -match '^\d+$' } |
        Sort-Object { [int64]$_.Name } -Descending |
        Select-Object -First 1
}

function Get-Prop {
    param($Object, [string]$Name)
    if ($null -eq $Object) { return $null }
    $prop = $Object.PSObject.Properties[$Name]
    if ($prop) { return $prop.Value }
    return $null
}

function ConvertTo-PythonStringLiteral {
    param([string]$Value)
    $escaped = $Value.
        Replace('\', '\\').
        Replace('"', '\"').
        Replace("`r", '\r').
        Replace("`n", '\n').
        Replace("`t", '\t')
    return '"' + $escaped + '"'
}

function ConvertTo-PythonLiteral {
    param($Value, [int]$Depth = 0)

    $indent = "  " * $Depth
    $nextIndent = "  " * ($Depth + 1)

    if ($null -eq $Value) { return "None" }
    if ($Value -is [bool]) {
        if ($Value) { return "True" }
        return "False"
    }
    if ($Value -is [string]) { return ConvertTo-PythonStringLiteral $Value }
    if ($Value -is [byte] -or $Value -is [sbyte] -or
        $Value -is [int16] -or $Value -is [uint16] -or
        $Value -is [int32] -or $Value -is [uint32] -or
        $Value -is [int64] -or $Value -is [uint64] -or
        $Value -is [single] -or $Value -is [double] -or $Value -is [decimal]) {
        return [System.Convert]::ToString($Value, [System.Globalization.CultureInfo]::InvariantCulture)
    }
    if ($Value -is [System.Collections.IDictionary]) {
        if ($Value.Count -eq 0) { return "{}" }
        $items = New-Object System.Collections.ArrayList
        foreach ($key in $Value.Keys) {
            [void]$items.Add($nextIndent + (ConvertTo-PythonLiteral ([string]$key)) + ": " + (ConvertTo-PythonLiteral $Value[$key] ($Depth + 1)))
        }
        return "{`n" + ($items -join ",`n") + "`n$indent}"
    }
    if ($Value -is [System.Collections.IEnumerable]) {
        $values = @($Value)
        if ($values.Count -eq 0) { return "[]" }
        $items = New-Object System.Collections.ArrayList
        foreach ($item in $values) {
            [void]$items.Add($nextIndent + (ConvertTo-PythonLiteral $item ($Depth + 1)))
        }
        return "[`n" + ($items -join ",`n") + "`n$indent]"
    }

    $props = @($Value.PSObject.Properties | Where-Object { $_.MemberType -eq "NoteProperty" -or $_.MemberType -eq "Property" })
    if ($props.Count -gt 0) {
        $items = New-Object System.Collections.ArrayList
        foreach ($prop in $props) {
            [void]$items.Add($nextIndent + (ConvertTo-PythonLiteral ([string]$prop.Name)) + ": " + (ConvertTo-PythonLiteral $prop.Value ($Depth + 1)))
        }
        return "{`n" + ($items -join ",`n") + "`n$indent}"
    }

    return ConvertTo-PythonStringLiteral ([string]$Value)
}

function Normalize-Caliber {
    param($Value)
    if ($null -eq $Value) { return $null }
    try { $v = [double]$Value } catch { return $null }
    if ($v -le 0) { return $null }
    if ($v -lt 5) { $v *= 1000 }
    elseif ($v -lt 80) { $v *= 10 }
    return [Math]::Round($v, 1)
}

function Add-UniqueNumber {
    param([System.Collections.ArrayList]$List, $Value, [double]$MaxValue = 1000)
    if ($null -eq $Value) { return }
    try { $v = [double]$Value } catch { return }
    if ($v -le 0 -or $v -gt $MaxValue) { return }
    $v = [Math]::Round($v, 1)
    if (-not $List.Contains($v)) { [void]$List.Add($v) }
}

function Get-MaterialName {
    param([int]$MaterialId)
    if ($MaterialId -ge 0 -and $MaterialId -lt $CollisionMaterialNames.Count) {
        return $CollisionMaterialNames[$MaterialId]
    }
    return "unknown_$MaterialId"
}

function Test-BowMaterial {
    param([string]$Name)
    return $Name -match '(^|_)Bow($|_)|Bow$|^Bow_'
}

function Test-SternMaterial {
    param([string]$Name)
    return $Name -match '(^|_)St($|_)|^St_|Stern$'
}

function Add-ClassifiedArmor {
    param([hashtable]$Groups, [string]$MaterialName, [double]$Mm)

    if ($Mm -le 0) { return }
    $isBow = Test-BowMaterial $MaterialName
    $isStern = Test-SternMaterial $MaterialName
    $isBowOrStern = $isBow -or $isStern
    $platingMax = 80
    $sideMax = 320

    if ($isBowOrStern -and $MaterialName -match 'Belt') {
        Add-UniqueNumber $Groups.belt $Mm
        if ($isBow) { Add-UniqueNumber $Groups.bowBelt $Mm }
        if ($isStern) { Add-UniqueNumber $Groups.sternBelt $Mm }
    }

    $isBowSternPlating = $MaterialName -match 'ConstrSide|Deck|Fdck|SideBow|DeckBow|SideStern|DeckStern'
    if ($isBow -and $isBowSternPlating -and $MaterialName -notmatch 'Belt|Bottom|Bulge|Inclin|Trans|Art|Cit') {
        Add-UniqueNumber $Groups.bow $Mm $platingMax
    }
    if ($isStern -and $isBowSternPlating -and $MaterialName -notmatch 'Belt|Bottom|Bulge|Inclin|Trans|Art|Cit') {
        Add-UniqueNumber $Groups.stern $Mm $platingMax
    }

    if (-not $isBowOrStern -and $MaterialName -match 'Deck|Fdck|Hang' -and
        $MaterialName -notmatch 'Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Bottom|Trans|Inclin') {
        Add-UniqueNumber $Groups.deck $Mm $platingMax
    }

    if (-not $isBowOrStern -and $MaterialName -match 'ConstrSide|Side|Belt' -and
        $MaterialName -notmatch 'Cit|OCit|Tur|Art|Bridge|Funnel|Kdp|Rudder|Bulge|Bottom|SS_|SSC|SideSS') {
        Add-UniqueNumber $Groups.side $Mm $sideMax
    }
}

function New-ArmorGroups {
    return @{
        bow = New-Object System.Collections.ArrayList
        stern = New-Object System.Collections.ArrayList
        deck = New-Object System.Collections.ArrayList
        side = New-Object System.Collections.ArrayList
        belt = New-Object System.Collections.ArrayList
        bowBelt = New-Object System.Collections.ArrayList
        sternBelt = New-Object System.Collections.ArrayList
    }
}

function Collect-Calibers {
    param($Object, [System.Collections.ArrayList]$Values, [int]$Depth = 0)
    if ($Depth -gt 7 -or $null -eq $Object) { return }
    if ($Object -is [System.Array]) {
        foreach ($item in $Object) { Collect-Calibers $item $Values ($Depth + 1) }
        return
    }
    foreach ($prop in $Object.PSObject.Properties) {
        if ($prop.Name -eq "barrelDiameter") {
            $caliber = Normalize-Caliber $prop.Value
            if ($caliber -and $caliber -ge 80 -and $caliber -le 600) {
                Add-UniqueNumber $Values $caliber 600
            }
        }
        if ($prop.Value -and ($prop.Value -isnot [string]) -and $Depth -lt 7) {
            Collect-Calibers $prop.Value $Values ($Depth + 1)
        }
    }
}

function Find-MainGunCaliber {
    param($Entry)
    $values = New-Object System.Collections.ArrayList
    Collect-Calibers $Entry $values
    if ($values.Count -eq 0) { return $null }
    return @($values | Sort-Object -Descending)[0]
}

function Convert-ProjectileRecordFromLines {
    param([string]$EntryName, [System.Collections.ArrayList]$Lines)

    $ammoType = $null
    $hePen = $null
    $sapPen = $null
    $caliber = $null

    foreach ($line in $Lines) {
        if ($line -match '"ammoType": "([^"]+)"') {
            $ammoType = $Matches[1]
        } elseif ($line -match '"alphaPiercingHE": ([0-9.]+)') {
            try { $hePen = [double]$Matches[1] } catch { $hePen = $null }
        } elseif ($line -match '"alphaPiercingCS": ([0-9.]+)') {
            try { $sapPen = [double]$Matches[1] } catch { $sapPen = $null }
        } elseif ($line -match '"bulletDiametr": ([0-9.]+)') {
            $caliber = Normalize-Caliber $Matches[1]
        }
    }

    $pen = $null
    if ($ammoType -eq "HE" -and $hePen -and $hePen -gt 0) {
        $pen = [Math]::Round($hePen, 1)
    } elseif ($ammoType -eq "CS" -and $sapPen -and $sapPen -gt 0) {
        $pen = [Math]::Round($sapPen, 1)
    } else {
        return $null
    }

    return [ordered]@{
        name = $EntryName
        ammoType = $ammoType
        penetrationMm = $pen
        caliberMm = $caliber
    }
}

function Read-ProjectilePenetrationDatabase {
    param([string]$Path)

    $projectiles = @{}
    $capturing = $false
    $captureDepth = 0
    $entryName = $null
    $buffer = New-Object System.Collections.ArrayList
    $reader = [System.IO.File]::OpenText($Path)

    try {
        while (($line = $reader.ReadLine()) -ne $null) {
            if (-not $capturing -and $line -match '^  "([^"]+)": \{') {
                $candidate = $Matches[1]
                if ($candidate -match '^[A-Z][A-Z]P[A-Z]\d+') {
                    $capturing = $true
                    $captureDepth = 0
                    $entryName = $candidate
                    $buffer.Clear()
                    [void]$buffer.Add($line)
                    $captureDepth += Get-JsonDepthDelta $line
                }
            } elseif ($capturing) {
                [void]$buffer.Add($line)
                $captureDepth += Get-JsonDepthDelta $line
            } else {
                continue
            }

            if ($capturing -and $captureDepth -eq 0) {
                $record = Convert-ProjectileRecordFromLines $entryName $buffer
                if ($record) {
                    $projectiles[$entryName] = $record
                }
                $capturing = $false
                $captureDepth = 0
                $entryName = $null
                $buffer.Clear()
            }
        }
    }
    finally {
        $reader.Close()
    }

    return $projectiles
}

function Find-MainGunAmmoPenetration {
    param(
        [System.Collections.ArrayList]$AmmoNames,
        [hashtable]$ProjectilePenByName,
        $MainGunCaliberMm,
        [string]$AmmoType
    )

    if ($null -eq $AmmoNames -or $AmmoNames.Count -eq 0) { return $null }
    if ($null -eq $ProjectilePenByName) { return $null }

    $values = New-Object System.Collections.ArrayList
    foreach ($ammoName in @($AmmoNames | Sort-Object -Unique)) {
        if (-not $ProjectilePenByName.ContainsKey($ammoName)) { continue }
        $projectile = $ProjectilePenByName[$ammoName]
        if ($projectile.ammoType -ne $AmmoType) { continue }
        if ($MainGunCaliberMm -and $projectile.caliberMm) {
            if ([Math]::Abs([double]$projectile.caliberMm - [double]$MainGunCaliberMm) -gt 2) { continue }
        }
        Add-UniqueNumber $values $projectile.penetrationMm 1000
    }

    if ($values.Count -eq 0 -and $MainGunCaliberMm) {
        foreach ($ammoName in @($AmmoNames | Sort-Object -Unique)) {
            if (-not $ProjectilePenByName.ContainsKey($ammoName)) { continue }
            $projectile = $ProjectilePenByName[$ammoName]
            if ($projectile.ammoType -ne $AmmoType) { continue }
            Add-UniqueNumber $values $projectile.penetrationMm 1000
        }
    }

    if ($values.Count -eq 0) { return $null }
    return @($values | Sort-Object -Descending)[0]
}

function Get-MainGunStatsFromLines {
    param([System.Collections.ArrayList]$Lines)

    $stack = New-Object System.Collections.ArrayList
    $calibers = New-Object System.Collections.ArrayList
    $ammoNames = New-Object System.Collections.ArrayList
    $depth = 0

    foreach ($line in $Lines) {
        $beforeDepth = $depth

        if ($line -match '^\s+"([^"]+)": \{') {
            $ctx = [pscustomobject]@{
                name = $Matches[1]
                depth = ($beforeDepth + 1)
                barrelDiameter = $null
                ammoNames = (New-Object System.Collections.ArrayList)
                collectingAmmo = $false
                ammoDepth = 0
                species = $null
                type = $null
            }
            [void]$stack.Add($ctx)
        }

        $top = if ($stack.Count -gt 0) { $stack[$stack.Count - 1] } else { $null }
        if ($top -and $line -match '"ammoList": \[') {
            $top.collectingAmmo = $true
            $top.ammoDepth = $beforeDepth + (Get-JsonDepthDelta $line)
        }

        for ($i = $stack.Count - 1; $i -ge 0; $i--) {
            $ctx = $stack[$i]
            if (-not $ctx.collectingAmmo) { continue }
            if ($line -match '^\s+"([^"]+)"[,]?$') {
                $ammoName = $Matches[1]
                if (-not $ctx.ammoNames.Contains($ammoName)) {
                    [void]$ctx.ammoNames.Add($ammoName)
                }
            }
            break
        }

        if ($top -and $line -match '"barrelDiameter": ([0-9.]+)') {
            $top.barrelDiameter = Normalize-Caliber $Matches[1]
        }

        if ($line -match '"species": "([^"]+)"') {
            for ($i = $stack.Count - 1; $i -ge 0; $i--) {
                $ctx = $stack[$i]
                if ($ctx.barrelDiameter -or $ctx.ammoNames.Count -gt 0) {
                    $ctx.species = $Matches[1]
                    break
                }
            }
        }

        if ($line -match '"type": "([^"]+)"') {
            for ($i = $stack.Count - 1; $i -ge 0; $i--) {
                $ctx = $stack[$i]
                if ($ctx.barrelDiameter -or $ctx.ammoNames.Count -gt 0) {
                    $ctx.type = $Matches[1]
                    break
                }
            }
        }

        $nextDepth = $depth + (Get-JsonDepthDelta $line)
        foreach ($ctx in $stack) {
            if ($ctx.collectingAmmo -and $nextDepth -lt $ctx.ammoDepth) {
                $ctx.collectingAmmo = $false
            }
        }

        while ($stack.Count -gt 0 -and $nextDepth -lt $stack[$stack.Count - 1].depth) {
            $ctx = $stack[$stack.Count - 1]
            $stack.RemoveAt($stack.Count - 1)
            if ($ctx.barrelDiameter -and $ctx.species -eq "Main" -and $ctx.type -eq "Gun") {
                Add-UniqueNumber $calibers $ctx.barrelDiameter 600
                foreach ($ammoName in $ctx.ammoNames) {
                    if (-not $ammoNames.Contains($ammoName)) {
                        [void]$ammoNames.Add($ammoName)
                    }
                }
            }
        }
        $depth = $nextDepth
    }

    while ($stack.Count -gt 0) {
        $ctx = $stack[$stack.Count - 1]
        $stack.RemoveAt($stack.Count - 1)
        if ($ctx.barrelDiameter -and $ctx.species -eq "Main" -and $ctx.type -eq "Gun") {
            Add-UniqueNumber $calibers $ctx.barrelDiameter 600
            foreach ($ammoName in $ctx.ammoNames) {
                if (-not $ammoNames.Contains($ammoName)) {
                    [void]$ammoNames.Add($ammoName)
                }
            }
        }
    }

    $maxCaliber = if ($calibers.Count -gt 0) { @($calibers | Sort-Object -Descending)[0] } else { $null }
    return [pscustomobject]@{
        maxCaliber = $maxCaliber
        ammoNames = $ammoNames
    }
}

function Find-HullObject {
    param($Entry)
    $candidates = @()
    foreach ($prop in $Entry.PSObject.Properties) {
        $value = $prop.Value
        if ($null -eq (Get-Prop $value "armor")) { continue }
        $model = Get-Prop $value "model"
        $hasHullLocation = $null -ne (Get-Prop $value "Hull")
        if ($prop.Name -match 'Hull' -or $hasHullLocation -or ($model -and $model.ToString() -match '/ship/')) {
            $score = 0
            if ($hasHullLocation) { $score += 20 }
            if ($prop.Name -match 'Hull') { $score += 10 }
            if ($prop.Name -match 'B_|B_Hull') { $score += 2 }
            if ($prop.Name -match 'C_|C_Hull') { $score += 3 }
            $candidates += [pscustomobject]@{ Name = $prop.Name; Value = $value; Score = $score }
        }
    }
    if ($candidates.Count -eq 0) { return $null }
    return ($candidates | Sort-Object Score, Name -Descending | Select-Object -First 1).Value
}

function Extract-ArmorGroups {
    param($Hull)
    $groups = New-ArmorGroups

    $armor = Get-Prop $Hull "armor"
    if ($null -eq $armor) { return $groups }

    foreach ($prop in $armor.PSObject.Properties) {
        try { $rawKey = [uint32]$prop.Name } catch { continue }
        try { $mm = [double]$prop.Value } catch { continue }
        $materialId = [int]($rawKey % 65536)
        $materialName = Get-MaterialName $materialId
        Add-ClassifiedArmor $groups $materialName $mm
    }
    return $groups
}

function Select-PrimaryArmorValues {
    param([System.Collections.ArrayList]$Values)
    $all = @($Values | Sort-Object -Unique)
    $primary = @($all | Where-Object { $_ -ge 10 })
    if ($primary.Count -gt 0) { return $primary }
    return $all
}

function Get-MinPrimaryArmorValue {
    param([System.Collections.ArrayList]$Values)
    $primary = @(Select-PrimaryArmorValues $Values)
    if ($primary.Count -gt 0) { return [double]$primary[0] }
    return $null
}

function Select-PrimaryDeckArmorValues {
    param(
        [System.Collections.ArrayList]$DeckValues,
        [System.Collections.ArrayList]$BowValues,
        [System.Collections.ArrayList]$SternValues,
        [System.Collections.ArrayList]$SideValues
    )

    $deck = @(Select-PrimaryArmorValues $DeckValues)
    if ($deck.Count -eq 0) { return $deck }

    $thresholds = New-Object System.Collections.ArrayList
    $bowMin = Get-MinPrimaryArmorValue $BowValues
    $sternMin = Get-MinPrimaryArmorValue $SternValues
    $sideMin = Get-MinPrimaryArmorValue $SideValues
    if ($null -ne $bowMin) { [void]$thresholds.Add($bowMin) }
    if ($null -ne $sternMin) { [void]$thresholds.Add($sternMin) }
    if ($null -ne $sideMin -and $sideMin -le 40) { [void]$thresholds.Add($sideMin) }

    $threshold = 10
    if ($thresholds.Count -gt 0) {
        $threshold = [double](($thresholds | Measure-Object -Maximum).Maximum)
    }

    foreach ($value in $deck) {
        if ([double]$value -ge $threshold) { return @([double]$value) }
    }
    return @([double]$deck[0])
}

function Select-PrimarySideArmorValues {
    param(
        [System.Collections.ArrayList]$SideValues,
        [System.Collections.ArrayList]$BeltValues
    )

    $side = @(Select-PrimaryArmorValues $SideValues)
    if ($side.Count -gt 0) { return $side }
    return @()
}

function Get-MaxPrimaryArmorValue {
    param([System.Collections.ArrayList]$Values)
    $primary = @(Select-PrimaryArmorValues $Values)
    if ($primary.Count -eq 0) { return 0 }
    return [double](($primary | Measure-Object -Maximum).Maximum)
}

function Select-ExtendedBowSternBelt {
    param(
        [System.Collections.ArrayList]$BowBeltValues,
        [System.Collections.ArrayList]$SternBeltValues,
        [System.Collections.ArrayList]$BowValues,
        [System.Collections.ArrayList]$SternValues
    )

    $bow = New-Object System.Collections.ArrayList
    $stern = New-Object System.Collections.ArrayList
    $values = New-Object System.Collections.ArrayList

    foreach ($value in @(Select-PrimaryArmorValues $BowBeltValues)) {
        Add-UniqueNumber $bow $value 1000
        Add-UniqueNumber $values $value 1000
    }
    foreach ($value in @(Select-PrimaryArmorValues $SternBeltValues)) {
        Add-UniqueNumber $stern $value 1000
        Add-UniqueNumber $values $value 1000
    }

    return [pscustomobject]@{
        values = @($values | Sort-Object -Unique)
        bow = @($bow | Sort-Object -Unique)
        stern = @($stern | Sort-Object -Unique)
    }
}

function Get-JsonDepthDelta {
    param([string]$Line)
    $delta = 0
    $inString = $false
    $escape = $false
    for ($i = 0; $i -lt $Line.Length; $i++) {
        $ch = $Line[$i]
        if ($escape) {
            $escape = $false
            continue
        }
        if ($ch -eq '\') {
            if ($inString) { $escape = $true }
            continue
        }
        if ($ch -eq '"') {
            $inString = -not $inString
            continue
        }
        if ($inString) { continue }
        if ($ch -eq '{' -or $ch -eq '[') { $delta++ }
        elseif ($ch -eq '}' -or $ch -eq ']') { $delta-- }
    }
    return $delta
}

function Convert-ShipEntry {
    param([string]$EntryName, [System.Collections.ArrayList]$Lines)
    if ($Lines.Count -eq 0) { return $null }
    $copy = @($Lines)
    $copy[$copy.Count - 1] = $copy[$copy.Count - 1] -replace ',\s*$', ''
    $json = "{`n" + ($copy -join "`n") + "`n}"
    $root = $json | ConvertFrom-Json
    return Get-Prop $root $EntryName
}

function Convert-Record {
    param([string]$EntryName, $Entry)
    $typeInfo = Get-Prop $Entry "typeinfo"
    if ((Get-Prop $typeInfo "type") -ne "Ship") { return $null }

    $hull = Find-HullObject $Entry
    $groups = if ($hull) { Extract-ArmorGroups $hull } else { Extract-ArmorGroups $null }
    $name = Get-Prop $Entry "name"
    if (-not $name) { $name = $EntryName }
    $caliber = Find-MainGunCaliber $Entry
    $extendedBelt = Select-ExtendedBowSternBelt $groups.bowBelt $groups.sternBelt $groups.bow $groups.stern
    $sideValues = @(Select-PrimarySideArmorValues $groups.side $groups.belt)

    $aliases = New-Object System.Collections.ArrayList
    foreach ($alias in @($EntryName, (Get-Prop $Entry "index"), (Get-Prop $Entry "id"), $name)) {
        if ($alias -and -not $aliases.Contains([string]$alias)) { [void]$aliases.Add([string]$alias) }
    }

    return [ordered]@{
        name = [string]$name
        aliases = @($aliases)
        mainGunCaliberMm = $caliber
        armor = [ordered]@{
            bowStern = [ordered]@{
                bow = @(Select-PrimaryArmorValues $groups.bow)
                stern = @(Select-PrimaryArmorValues $groups.stern)
            }
            deck = [ordered]@{ values = @(Select-PrimaryDeckArmorValues $groups.deck $groups.bow $groups.stern $sideValues) }
            side = [ordered]@{ values = $sideValues }
            extendedBowSternBelt = [ordered]@{
                present = ($extendedBelt.values.Count -gt 0)
                values = @($extendedBelt.values)
                bow = @($extendedBelt.bow)
                stern = @($extendedBelt.stern)
            }
        }
    }
}

function Convert-RecordFromLines {
    param([string]$EntryName, [System.Collections.ArrayList]$Lines, [hashtable]$ProjectilePenByName)

    $isShip = $false
    $name = $EntryName
    $index = $null
    $id = $null
    $mainGunStats = Get-MainGunStatsFromLines $Lines
    $maxCaliber = $mainGunStats.maxCaliber
    $ammoNames = $mainGunStats.ammoNames
    $selectedGroups = New-ArmorGroups
    $currentGroups = $null
    $inHull = $false
    $hullDepth = 0
    $inArmor = $false
    $armorDepth = 0

    foreach ($line in $Lines) {
        if ($line -match '^\s+"type": "Ship"') {
            $isShip = $true
        }
        if ($line -match '^    "name": "([^"]+)"') {
            $name = $Matches[1]
        } elseif ($line -match '^    "index": "([^"]+)"') {
            $index = $Matches[1]
        } elseif ($line -match '^    "id": ([0-9]+)') {
            $id = $Matches[1]
        }

        if (-not $inHull -and $line -match '^    "([^"]*Hull[^"]*)": \{') {
            $inHull = $true
            $hullDepth = 0
            $currentGroups = New-ArmorGroups
        }

        if ($inHull -and -not $inArmor -and $line -match '^      "armor": \{') {
            $inArmor = $true
            $armorDepth = 0
        } elseif ($inArmor -and $line -match '^        "([0-9]+)": ([0-9.]+)') {
            try { $rawKey = [uint32]$Matches[1] } catch { $rawKey = $null }
            try { $mm = [double]$Matches[2] } catch { $mm = 0 }
            if ($null -ne $rawKey) {
                $materialId = [int]($rawKey % 65536)
                $materialName = Get-MaterialName $materialId
                Add-ClassifiedArmor $currentGroups $materialName $mm
            }
        }

        if ($inArmor) {
            $armorDepth += Get-JsonDepthDelta $line
            if ($armorDepth -eq 0) {
                $inArmor = $false
            }
        }
        if ($inHull) {
            $hullDepth += Get-JsonDepthDelta $line
            if ($hullDepth -eq 0) {
                $selectedGroups = $currentGroups
                $currentGroups = $null
                $inHull = $false
                $inArmor = $false
            }
        }
    }

    if (-not $isShip) { return $null }

    $hePen = Find-MainGunAmmoPenetration $ammoNames $ProjectilePenByName $maxCaliber "HE"
    $sapPen = Find-MainGunAmmoPenetration $ammoNames $ProjectilePenByName $maxCaliber "CS"
    $extendedBelt = Select-ExtendedBowSternBelt $selectedGroups.bowBelt $selectedGroups.sternBelt $selectedGroups.bow $selectedGroups.stern
    $sideValues = @(Select-PrimarySideArmorValues $selectedGroups.side $selectedGroups.belt)

    $aliases = New-Object System.Collections.ArrayList
    foreach ($alias in @($EntryName, $index, $id, $name)) {
        if ($alias -and -not $aliases.Contains([string]$alias)) { [void]$aliases.Add([string]$alias) }
    }

    return [ordered]@{
        name = [string]$name
        aliases = @($aliases)
        mainGunCaliberMm = $maxCaliber
        mainGunHePenMm = $hePen
        mainGunSapPenMm = $sapPen
        armor = [ordered]@{
            bowStern = [ordered]@{
                bow = @(Select-PrimaryArmorValues $selectedGroups.bow)
                stern = @(Select-PrimaryArmorValues $selectedGroups.stern)
            }
            deck = [ordered]@{ values = @(Select-PrimaryDeckArmorValues $selectedGroups.deck $selectedGroups.bow $selectedGroups.stern $sideValues) }
            side = [ordered]@{ values = $sideValues }
            extendedBowSternBelt = [ordered]@{
                present = ($extendedBelt.values.Count -gt 0)
                values = @($extendedBelt.values)
                bow = @($extendedBelt.bow)
                stern = @($extendedBelt.stern)
            }
        }
    }
}

function Get-Realm {
    param([string]$GameDir, [string]$ExplicitRealm)
    if ($ExplicitRealm) { return $ExplicitRealm.ToUpperInvariant() }
    $realmPath = Join-Path $GameDir "currentrealm.txt"
    if (Test-Path $realmPath) {
        $value = (Get-Content -LiteralPath $realmPath -Raw).Trim()
        if ($value) { return $value.ToUpperInvariant() }
    }
    return "ASIA"
}

function Resolve-WowsUnpack {
    param([string]$ProjectRoot, [string]$Requested)
    if ($Requested) { return $Requested }
    $local = Join-Path $ProjectRoot "tools\wowsunpack-git\bin\wowsunpack.exe"
    if (Test-Path $local) { return $local }
    return "wowsunpack"
}

$buildDir = Get-LatestBuildDir $GameDir
if (-not $buildDir) { throw "No game build directory found under $GameDir\bin" }

$realmId = Get-Realm $GameDir $Realm
$WowsUnpack = Resolve-WowsUnpack $ProjectRoot $WowsUnPack
$work = Join-Path $ProjectRoot "build\gameparams"
if (-not $OutPath) {
    $OutPath = Join-Path $ProjectRoot "src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json"
}
New-Item -ItemType Directory -Force -Path $work | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $OutPath) | Out-Null

if (-not $GameParamsJson) {
    $localBuildCandidate = Join-Path $work "GameParams_$($buildDir.Name)_$realmId.json"
    $tmpBuildCandidate = "C:\tmp\GameParams_$($buildDir.Name)_$realmId.json"
    $localCandidate = Join-Path $work "GameParams_$realmId.json"
    $tmpCandidate = "C:\tmp\GameParams_$realmId.json"
    if (Test-Path $localBuildCandidate) {
        $GameParamsJson = $localBuildCandidate
    } elseif (Test-Path $tmpBuildCandidate) {
        $GameParamsJson = $tmpBuildCandidate
    } elseif (Test-Path $localCandidate) {
        $GameParamsJson = $localCandidate
    } elseif (Test-Path $tmpCandidate) {
        $GameParamsJson = $tmpCandidate
    } elseif ($ExtractGameParams) {
        $GameParamsJson = $localBuildCandidate
    } else {
        throw "No GameParams JSON found. Provide -GameParamsJson or rerun with -ExtractGameParams. Extraction can use significant memory, so it is opt-in."
    }
}

if ($ExtractGameParams -and -not (Test-Path $GameParamsJson)) {
    Write-Host "Extracting GameParams realm $realmId via wowsunpack..."
    & $WowsUnpack --game-dir $GameDir game-params --id $realmId $GameParamsJson
    if ($LASTEXITCODE -ne 0) {
        throw "wowsunpack failed with exit code $LASTEXITCODE"
    }
}

if (-not (Test-Path $GameParamsJson)) {
    throw "GameParams JSON not found: $GameParamsJson"
}

$fastGenerator = Join-Path $PSScriptRoot "generate-armor-db-fast.mjs"
$node = Get-Command node -ErrorAction SilentlyContinue
if ($node -and (Test-Path $fastGenerator) -and -not $env:APOA_FORCE_PS_GENERATOR) {
    $nodeArgs = @(
        $fastGenerator,
        "--game-dir", $GameDir,
        "--project-root", $ProjectRoot,
        "--game-params-json", $GameParamsJson,
        "--out-path", $OutPath,
        "--realm", $realmId,
        "--override-path", $OverridePath
    )
    if ($ShipKeyFilter) { $nodeArgs += @("--ship-key-filter", $ShipKeyFilter) }
    if ($MaxShips -gt 0) { $nodeArgs += @("--max-ships", [string]$MaxShips) }

    & $node.Source @nodeArgs
    if ($LASTEXITCODE -ne 0) {
        throw "generate-armor-db-fast.mjs failed with exit code $LASTEXITCODE"
    }
    return
}

Write-Host "Streaming $GameParamsJson..."
$projectilePenByName = Read-ProjectilePenetrationDatabase $GameParamsJson
Write-Host "Collected $($projectilePenByName.Count) HE/SAP projectile penetration records."

$ships = [ordered]@{}
$capturing = $false
$captureDepth = 0
$entryName = $null
$buffer = New-Object System.Collections.ArrayList
$reader = [System.IO.File]::OpenText($GameParamsJson)

try {
    while (($line = $reader.ReadLine()) -ne $null) {
        if (-not $capturing -and $line -match '^  "([^"]+)": \{') {
            $candidate = $Matches[1]
            $isShipKey = $candidate -match '^P[A-Z]S[A-Z]'
            $matchesFilter = (-not $ShipKeyFilter) -or ($candidate -like $ShipKeyFilter)
            if ($isShipKey -and $matchesFilter) {
                $capturing = $true
                $captureDepth = 0
                $entryName = $candidate
                $buffer.Clear()
                [void]$buffer.Add($line)
                $captureDepth += Get-JsonDepthDelta $line
            }
        } elseif ($capturing) {
            [void]$buffer.Add($line)
            $captureDepth += Get-JsonDepthDelta $line
        } else {
            continue
        }

        if ($capturing -and $captureDepth -eq 0) {
            $record = Convert-RecordFromLines $entryName $buffer $projectilePenByName
            if ($record) {
                $ships[$entryName] = $record
                if (($ships.Count % 50) -eq 0) {
                    Write-Host "  parsed $($ships.Count) ships..."
                }
            }
            $capturing = $false
            $captureDepth = 0
            $entryName = $null
            $buffer.Clear()
            if ($MaxShips -gt 0 -and $ships.Count -ge $MaxShips) { break }
        }
    }
}
finally {
    $reader.Close()
}

if (Test-Path $OverridePath) {
    Write-Host "Applying overrides from $OverridePath..."
    $overrides = Get-Content -LiteralPath $OverridePath -Raw | ConvertFrom-Json
    $overrideShips = Get-Prop $overrides "ships"
    if ($overrideShips) {
        foreach ($prop in $overrideShips.PSObject.Properties) {
            $ships[$prop.Name] = $prop.Value
        }
    }
}

$database = [ordered]@{
    schema = 2
    meta = [ordered]@{
        name = "14.3-helper"
        gameBuild = $buildDir.Name
        realm = $realmId
        generatedAt = (Get-Date).ToString("s")
        source = "wowsunpack GameParams JSON, streamed per ship"
        notes = "Armor groups are classified from collision material IDs. Deck uses a representative weather-deck thickness rather than every deck-like material. Side means upper side plating above the main armor belt. Main-gun HE/SAP penetration is resolved from projectile alphaPiercingHE/alphaPiercingCS and filtered by the largest main-gun caliber. Extraction is opt-in to avoid high memory use."
    }
    ships = $ships
}

$json = $database | ConvertTo-Json -Depth 30
[System.IO.File]::WriteAllText($OutPath, $json, [System.Text.Encoding]::UTF8)
$pyOutPath = [System.IO.Path]::ChangeExtension($OutPath, ".py")
$pyLiteral = ConvertTo-PythonLiteral $database
$pyText = "# -*- coding: utf-8 -*-`n# Generated from armor_overmatch.json. WoWS ModsAPI blocks the json module.`nDATABASE = $pyLiteral`n"
[System.IO.File]::WriteAllText($pyOutPath, $pyText, [System.Text.Encoding]::UTF8)
Write-Host "Wrote $($ships.Count) ships to $OutPath"
Write-Host "Wrote Python database to $pyOutPath"
