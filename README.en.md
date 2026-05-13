# 14.3-helper

Aslain-compatible World of Warships battle UI mod for showing armor interaction
against the current aim-assist target.

The mod uses the normal WoWS ModAPI/DataHub path used by existing PnFMods. It
does not inject code into the game process, read hidden enemies, or calculate
aiming solutions. It evaluates local reference data against the current target.

## UI Behavior

The panel is hidden unless the player has a valid enemy aim-assist target.

- AP: shows overmatch status using `caliber_mm / 14.3 >= armor_mm`.
- HE: shows penetration status using `mainGunHePenMm >= armor_mm`.
- SAP: shows penetration status using `mainGunSapPenMm >= armor_mm`.
- Torpedo/depth-charge weapon state: hidden.

Rows:

- Bow/Stern
- Deck
- Side
- Extended bow/stern belt / icebreaker

Mixed armor groups show partial status instead of being collapsed to a single
yes/no result.

The in-battle panel is multilingual. English is the default for modpack
distribution. Simplified Chinese remains supported through the stored
`apOvermatchAssistantLanguage` preference, but this standalone archive does not
bundle a TTaro settings UI.

The Aslain archive is standalone for battle use: it includes the PnFMods loader,
ModsInstaller, and the battle UI. It intentionally does not bundle TTaro config
center files, so it will not overwrite another mod's shared TTaro panel. It does
not require any other installed mod to provide TTaro or draggable helpers.

## Layout

```text
src/res_mods/PnFMods/APOvermatchAssistant/Main.py
src/res_mods/PnFMods/APOvermatchAssistant/data/armor_overmatch.json
src/res_mods/PnFMods/ModsInstaller_4_3_1/Main.py
src/res_mods/PnFMods/ModsInstaller_4_3_1/ModsInstaller.py
src/res_mods/PnFMods/ModsInstaller_4_3_1/ResMgr.py
src/res_mods/gui/unbound2/PnFMods/APOvermatchAssistant.unbound
src/res_mods/PnFMods/ModsInstaller_4_3_1/mods/APOvermatchAssistant.xml
src/res_mods/PnFModsLoader.py
tools/generate-armor-db.ps1
tools/generate-armor-db-fast.mjs
tools/update-armor-db.ps1
tools/setup-wowsunpack.ps1
```

## Build

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\test-rule.ps1
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1
```

The Aslain custom mod archive is written to:

```text
dist\14.3-helper_Aslain.zip
```

## Local Install

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\install-local.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships"
```

## Armor Database Update

`update-armor-db.ps1` creates a candidate database, compares it with the
current database, writes diff reports, and only replaces the committed database
when `-Apply` is passed. The generator uses `tools/generate-armor-db-fast.mjs`
when `node` is available and falls back to PowerShell otherwise.

Report only:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships"
```

Report and apply:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships" `
  -Apply
```

If the cached GameParams JSON for the current build is missing, extract it
explicitly:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships" `
  -ExtractGameParams `
  -Apply
```

Extraction is opt-in because it is the only high-memory step. Generated
GameParams caches are build-specific under:

```text
build\gameparams\GameParams_<gameBuild>_<realm>.json
```

Diff outputs are written under:

```text
build\armor-update\armor_diff.<timestamp>.json
build\armor-update\armor_diff.<timestamp>.md
```

Quick sample check:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\generate-armor-db.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships" `
  -GameParamsJson "C:\tmp\GameParams_ASIA.json" `
  -ShipKeyFilter "PASB017_Montana_1945"
```

The generated Montana record should show 406 mm guns, HE 68 mm, bow/stern 32,
deck 38, side 38, and no extended bow/stern belt.
