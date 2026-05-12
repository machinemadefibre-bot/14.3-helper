# 14.3 Helper

[简体中文](README.md) | **English**

[![Version](https://img.shields.io/badge/version-0.2.26-blue.svg)](#release)
[![World of Warships](https://img.shields.io/badge/World%20of%20Warships-battle%20UI-informational.svg)](https://worldofwarships.com/)
[![Aslain custom mod](https://img.shields.io/badge/Aslain-custom%20mod-orange.svg)](https://aslain.com/)
[![License](https://img.shields.io/badge/license-TBD-lightgrey.svg)](#license)

**14.3 Helper** is an Aslain-compatible World of Warships battle UI mod that
shows whether your currently selected shell can defeat the locked target's key
external armor areas.

It is built for a narrow job: reduce armor-threshold memorization during battle
without adding aim prediction, hidden information, automation, or process
injection.

## Features

- Shows only when there is a valid locked / aim-assist target.
- Hides for torpedoes and other non-main-gun weapon states.
- Supports AP overmatch using the in-game `caliber / 14.3 >= armor` rule.
- Supports HE and SAP penetration checks against the same armor groups.
- Uses compact symbols instead of long combat text:
  - `√` means pass.
  - `×` means fail.
  - `△` means mixed / partial.
  - `?` means missing data.
- Rows shown in battle:
  - `艏艉`: bow and stern plating.
  - `甲板`: exposed deck / main weather deck.
  - `侧板`: upper side plating above the main belt.
  - `装甲延伸`: bow armor extension / icebreaker-style belt.
- Draggable overlay with adjustable opacity through the PnFMods / TTaro mod
  configuration UI.

## Safety Scope

This project follows the spirit of the official World of Warships mod policy:

- Uses the normal client mod structure: `res_mods`, `PnFMods`, and Unbound UI.
- Reads only the player's current battle state exposed through the client mod
  API / DataHub path.
- Uses a local, versioned armor reference database generated from the installed
  game client.
- Does not calculate lead, aim points, shell travel prediction, or target
  movement solutions.
- Does not read hidden ships, unrevealed positions, or server-only information.
- Does not patch game binaries, inject DLLs, or modify original game files.

Relevant policy references:

- [Wargaming World of Warships Mod Policy](https://wargaming.net/support/en/products/wows/article/10720/)
- [Wargaming Prohibited Software Policy](https://wargaming.net/support/en/products/wows/article/10721/)

This mod is not affiliated with, endorsed by, or approved by Wargaming.

## Install

### Aslain Custom Mods

Recommended for testing and distribution.

1. Download the release zip, for example `14.3-Helper_Aslain_v0.2.26.zip`.
2. Do not extract it.
3. Put the zip in:

```text
World of Warships\Aslain_Modpack\Custom_mods\
```

4. Run the Aslain installer again.
5. Launch the game and enter battle.

### Manual Install

Use this only if you are not installing through Aslain.

1. Extract the zip into the active game build directory:

```text
World of Warships\bin\<current_build>\
```

2. After extraction, these paths should exist:

```text
World of Warships\bin\<current_build>\res_mods\gui\unbound2\PnFMods\APOvermatchAssistant.unbound
World of Warships\bin\<current_build>\res_mods\PnFMods\APOvermatchAssistant\Main.py
```

## Usage

1. Enter a battle.
2. Select AP, HE, or SAP main guns.
3. Lock or aim-assist an enemy ship.
4. Read the four compact armor rows near the crosshair.

The panel is intentionally quiet. It does not show the target name, detailed
armor values, your penetration number, or long explanatory text during battle.

## Build

Requirements:

- Windows PowerShell
- Node.js for the fast database and Unbound generators
- `wowsunpack` only when extracting fresh client data

Run the rule tests and build the Aslain zip:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\test-rule.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\build.ps1
```

The package is written to:

```text
dist\APOvermatchAssistant_Aslain.zip
```

## Local Install For Development

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\install-local.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships"
```

## Armor Data Updates

The armor database is designed to be regenerated after each game update. Raw
client extraction can be memory-heavy, so extraction is opt-in.

Generate a diff report only:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships"
```

Generate the report and apply the updated database:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships" `
  -Apply
```

Extract fresh `GameParams` only when the cache for the current build is missing:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\tools\update-armor-db.ps1 `
  -GameDir "S:\SteamLibrary\steamapps\common\World of Warships" `
  -ExtractGameParams `
  -Apply
```

Generated diff reports are written under:

```text
build\armor-update\
```

Large extracted client caches are intentionally ignored by git.

## Project Layout

```text
src/res_mods/PnFMods/APOvermatchAssistant/Main.py
src/res_mods/PnFMods/APOvermatchAssistant/data/armor_overmatch.json
src/res_mods/PnFMods/APOvermatchAssistant/data/armor_overmatch.py
src/res_mods/gui/unbound2/PnFMods/APOvermatchAssistant.unbound
src/res_mods/PnFMods/ModsInstaller_4_3_1/mods/APOvermatchAssistant.xml
tools/build.ps1
tools/install-local.ps1
tools/update-armor-db.ps1
tools/generate-armor-db-fast.mjs
tools/normalize-deck-values.mjs
```

The internal module name is still `APOvermatchAssistant` for compatibility with
the existing PnFMods structure. The public project name is `14.3 Helper`.

## Reporting Bad Data

Please include these details when reporting an armor or shell mismatch:

- Game version / build.
- Your ship and selected ammo type.
- Locked target ship.
- Screenshot of the helper panel.
- Screenshot or note from the in-game armor viewer.
- Expected result for `艏艉`, `甲板`, `侧板`, or `装甲延伸`.

Good armor corrections should be reproducible from the current client data or
from the in-game armor viewer.

## Known Limits

- World of Warships updates can change UI APIs, ship IDs, armor labels, or shell
  data. Regenerate the database after major updates.
- Compatibility with every other UI mod is not guaranteed.
- Armor categories are condensed for battle readability. The detailed armor
  viewer remains the source of truth for exact model geometry.
- `?` means the local database or live battle state did not provide enough data
  for a reliable result.

## Release

Current test release:

```text
v0.2.26
```

Recommended release checklist:

1. Regenerate or diff armor data for the current game build.
2. Run `tools\test-rule.ps1`.
3. Run `tools\build.ps1`.
4. Upload the generated Aslain zip as a GitHub Release asset.
5. Test in a training room with AP, HE, SAP, and torpedoes.

## License

No open-source license has been declared yet. Until a license file is added,
all rights are reserved by the repository owner.
