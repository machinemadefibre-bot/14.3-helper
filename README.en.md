# 14.3-helper

[中文](README.md)

`14.3-helper` is an in-battle UI mod for World of Warships. It checks the shell you are currently using against the ship you are aiming at, then shows whether that shell can overmatch or penetrate several armor areas.

The current release package is standalone. When installed through Aslain `Custom_mods`, it does not require another TTaro, PnFMods, or helper mod to be installed first.

## Features

- AP: checks overmatch with `caliber / 14.3`.
- HE / SAP: checks penetration with the current shell penetration value.
- Battle-switchable display mode: `My gun` checks your current shell against the target, while `Enemy gun` checks whether the target ship's main guns can threaten your armor areas.
- In `Enemy gun` mode, targets with SAP use target SAP penetration first. Without SAP, target main guns below `283 mm` use HE penetration, while `283 mm` and larger guns use AP overmatch.
- The floating panel uses fixed white `ATK` / `DEF` prefixes for outgoing and incoming checks. Incoming checks color safety: `×` is green, `√` is red.
- Each battle starts with the last saved display mode. Holding Alt temporarily flips to the other mode, then returns when Alt is released.
- Shows separate checks for bow/stern, deck, side plating, and forward/aft extended belt.
- Extended belt is split into forward and aft results, for example `Ext Bow √ Stern ×`.
- Result colors are per armor area: green means pass, red means fail, yellow means mixed or borderline, gray means no data.
- Chinese and English UI text. The language setting is shown as `ZH` / `EN`.
- Supports dragging, scale, position lock, position reset, and background opacity.

The mod only uses current in-battle target data, current shell data, and a local armor database. It does not provide aim assist, does not reveal hidden enemies, and does not inject into the game process.

## In-Game Settings

In battle, the floating helper has a small gear button on its left side. Click it to open the `14.3-helper` settings page.

Available settings:

- Language: `ZH` / `EN`
- Display mode: `My gun` / `Enemy gun`
- Alt temporary switch: hold Alt to invert the current display mode without changing the saved default
- UI scale
- Drag lock
- Reset position
- Background opacity

If the top-left TTaro settings panel is visible, `14.3-helper` can also be selected there.

## Installation

### Aslain Custom Mods

1. Download `14.3-helper_Aslain.zip` from GitHub Releases.
2. Put it into:

```text
World of Warships\Aslain_Modpack\Custom_mods
```

3. Run the Aslain Modpack installer.
4. Enter a battle and check the floating panel and the settings button.

### Local Test Install

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\install-local.ps1 -GameDir "S:\SteamLibrary\steamapps\common\World of Warships"
```

The script copies the files into the latest numeric `bin\<version>\res_mods`
folder. If `gui\battle_elements.xml` already exists there, it also patches the
`OA_APOvermatchAssistant` battle UI entry directly; otherwise the bundled
`ModsInstaller_4_3_1` will patch it when the game starts.

## Build

Run the full test entrypoint when Python is available:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\test.ps1 -Build
```

Run the rule check directly when you only need the armor-rule regression suite:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\test-rule.ps1
```

Then build the Aslain package:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1
```

The output is:

```text
dist\14.3-helper_Aslain.zip
```

To build and put the exact package into Aslain `Custom_mods` in one step:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1 -AslainCustomModsDir "S:\SteamLibrary\steamapps\common\World of Warships\Aslain_Modpack\Custom_mods"
```

## Updating Armor Data

Armor data lives in:

```text
src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json
```

Use the one-click update entry for normal version refreshes:

```text
tools\update-armor-db-and-build.exe
```

Double-click it to open a command window and run the full workflow:

1. Generate a candidate database from the current game version.
2. Print added, removed, and changed ships/fields.
3. Wait for `Y` / `N` confirmation.
4. Replace the current database only after `Y`, backing up the old database to `tools\armor_snapshots`.
5. Run the rule tests.
6. Build the package into `dist`.

The output zip gets a game-patch suffix:

```text
dist\14.3-helper_Aslain-patch<game version>.zip
```

Type `N` if you only want to inspect the diff. The candidate database and diff files remain under:

```text
build\armor-update
```

Run the PowerShell workflow directly when you need custom arguments. For example, to reuse an existing GameParams JSON:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\update-armor-db-and-build.ps1 -GameParamsJson "C:\tmp\GameParams_ASIA.json"
```

The lower-level report script is `tools\update-armor-db.ps1`. Without `-Apply`, it only writes a report. With `-Apply`, it replaces the database. `-ExtractGameParams` extracts fresh data from game files and can use a lot of memory, so reserve it for game-version refreshes.

## Accuracy Notice

The whole program was vibe-coded with AI assistance. It has been manually tested, but not against every ship, every armor piece, or every game-version change, so it does not promise 100% accuracy.

The armor database combines extracted geometry, positional filtering, and manual correction rules. Complex layouts can still be wrong, especially extended belts, minor deck plates, underwater armor, and carrier side plating.

If you find a wrong result, please open an issue with:

- Ship name and game client language
- Shell type and gun caliber
- Screenshot of the in-game armor view
- Result shown by the mod

## Repository Layout

```text
src\
  res_mods\
    PnFMods\
      APOvermatchAssistant\      # Loader entry, helper modules, and armor database
      ModsInstaller_4_3_1\       # UI patcher required for standalone install
    gui\
      unbound2\
        PnFMods\                 # Floating panel and settings UI
        mods\                    # Drag helper
tools\                           # Build, install, and armor-data scripts
dist\                            # Local release artifacts, not committed
```
