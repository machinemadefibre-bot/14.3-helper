# 14.3-helper

[中文](README.md)

`14.3-helper` is an in-battle UI mod for World of Warships. It reads your selected shell, locked target, ship data, and the local armor database, then shows whether that shell can overmatch or penetrate key armor areas.

The current release package is standalone. When installed through Aslain `Custom_mods`, it does not require TTaro, PnFMods, or any other helper mod to be installed first.

## Features

- AP overmatch: checks `caliber / 14.3` first. If AP overmatches, it is treated as a penetration.
- AP penetration: when overmatch does not apply, the mod uses unpacked AP shell parameters and a precomputed penetration table, combined with current range, impact angle, target relative heading, belt inclination, and belt heading-angle range.
- Main-belt angle: when the target is locked and visible, the mod reads own and target `mapPosition.position/yaw` and calculates the target relative heading in real time.
- Main-belt data: battleships, cruisers, carriers, and similar ships use extracted main-belt thickness and inclination ranges. Missing main-belt data falls back to side plating as an estimate. Destroyers use side plating as the main belt for AP checks when they have no separate belt.
- Submarine targets: the panel is hidden when the locked target is a submarine.
- HE / SAP: checks penetration with the current shell penetration value.
- `My gun` / `Enemy gun`: `My gun` checks your selected shell against the target. `Enemy gun` checks whether the target ship's main guns can threaten your armor.
- `Enemy gun` mode rules: target SAP is preferred when available. Without SAP, target guns below `283 mm` use HE penetration, while `283 mm` and larger guns use AP overmatch.
- AP display rules: depending on AP impact angle and relative heading, the panel narrows the rows to the currently relevant deck/side, main belt, or bow/stern and extended-belt overmatch checks.
- Result symbols: `√` means penetrates, `×` means does not penetrate, `△` means borderline or mixed, and `?` means missing data.
- AP uncertainty band: penetration checks keep about a `5%` margin so fitted formula edge cases are not shown as overly certain.
- Panel text: main text stays fixed white, with `ATK` / `DEF` for outgoing and incoming views. Result symbols remain compact and color-coded.
- Chinese and English UI text. The language setting is shown as `ZH` / `EN`.
- Supports dragging, scale, position lock, position reset, background opacity, and an off-by-default loaded/debug indicator.

The mod only reads current in-battle target data, current shell data, and a local database. It does not provide aim assist, does not reveal hidden enemies, and does not inject into the game process.

## In-Game Settings

In battle, the floating helper has a small `CFG` button on its left side. Click it to open the built-in `14.3-helper` settings page. This entry does not depend on TTaro, so the main panel should still render if TTaro files are missing or overwritten by another mod.

Available settings:

- Language: `ZH` / `EN`
- Display mode: `My gun` / `Enemy gun`
- Alt temporary switch: hold Alt to invert the current display mode without changing the saved default
- UI scale
- Drag lock
- Reset position
- Background opacity
- Loaded/debug indicator: off by default, useful only when diagnosing "mod not loaded" versus "no usable target"

If the top-left TTaro settings panel is visible, `14.3-helper` can also be selected there.

## Installation

### Aslain Custom Mods

1. Download the Aslain zip from GitHub Releases, for example `14.3-helper_v0.5.1_Aslain-patch15.5.zip`.
2. Put the zip file directly into:

```text
World of Warships\Aslain_Modpack\Custom_mods
```

3. Run the Aslain Modpack installer.
4. Enter a battle and check the floating panel, settings button, and target-lock display.

The zip starts at `res_mods\...`, so placing it in `Custom_mods` is enough for a one-pass install.

If an older same-name install skipped the UI patch, installing `0.5.1` forces ModsInstaller to run the patch again. To diagnose a missing battle panel, check whether `res_mods\gui\battle_elements.xml` contains `elementName="OA_APOvermatchAssistant"`.

### Local Test Install

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\install-local.ps1 -GameDir "S:\SteamLibrary\steamapps\common\World of Warships"
```

The script copies the files into the latest numeric `bin\<version>\res_mods` folder. If `gui\battle_elements.xml` already exists there, it also patches the `OA_APOvermatchAssistant` battle UI entry directly; otherwise the bundled `ModsInstaller_4_3_1` will patch it when the game starts.

## Build

Run the full test entrypoint:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\test.ps1
```

Run only the armor-rule regression suite:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\test-rule.ps1
```

Build the Aslain package:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1
```

The build script prompts for the game patch suffix. Press Enter to use the project target game version `15.5`, or pass it explicitly:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1 -PatchVersion 15.5
```

Example output:

```text
dist\14.3-helper_v0.5.1_Aslain-patch15.5.zip
```

To build and copy the exact package into Aslain `Custom_mods` in one step:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1 -PatchVersion 15.5 -AslainCustomModsDir "S:\SteamLibrary\steamapps\common\World of Warships\Aslain_Modpack\Custom_mods"
```

## Updating Armor Data

Armor data lives in:

```text
src\res_mods\PnFMods\APOvermatchAssistant\data\armor_overmatch.json
```

Use the unified update entry for normal game-version refreshes:

```text
tools\update-armor-db-and-build.exe
```

Double-click it to open a command window. The menu includes:

- Update the database and build a zip
- Manually edit armor data
- Extract and analyze main belts
- Exit

The update workflow:

1. Generates a candidate database from the current game version.
2. Extracts AP shell parameters, HE/SAP penetration, armor thickness, main-belt inclination, and belt heading-angle ranges.
3. Prints added, removed, and changed ships/fields.
4. Waits for `Y` / `N` confirmation.
5. Replaces the current database only after `Y`, backing up the old database to `tools\armor_snapshots`.
6. Syncs the Python database and the embedded Unbound database.
7. Runs tests.
8. Builds the package into `dist`.

Type `N` if you only want to inspect the diff. The candidate database and diff files remain under:

```text
build\armor-update
```

Run the PowerShell workflow directly when you need custom arguments. For example, to reuse an existing GameParams JSON:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\update-armor-db-and-build.ps1 -GameParamsJson "C:\tmp\GameParams_ASIA.json"
```

The lower-level report script is `tools\update-armor-db.ps1`. Without `-Apply`, it only writes a report. With `-Apply`, it replaces the database. `-ExtractGameParams` extracts fresh data from game files and can use a lot of memory, so reserve it for game-version refreshes.

### Automatic Steam Version Check

`tools\check-steam-wows-update.ps1` performs unattended Steam installation checks, armor database updates, full tests, and packaging. It only changes and locally commits allowlisted generated files on a clean `develop`; it never pushes.

The daily run does not use Codex Scheduled. `tools\install-wows-update-task.ps1` creates an isolated `develop` worktree and registers a Windows task that runs every day at 08:00 local time. `NO_UPDATE` and incomplete Steam downloads stay silent. Only a ready package, a build failure, or another actionable condition causes `tools\run-wows-update-task.ps1` to create one persistent Codex task for a mobile notification. Codex only reports the result: it does not browse, upload, or post. The zip is copied to the main checkout's `dist` for manual publication.

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\check-steam-wows-update.ps1 -Mode SelfTest
powershell -ExecutionPolicy Bypass -File .\tools\check-steam-wows-update.ps1 -Mode DryRun
powershell -ExecutionPolicy Bypass -File .\tools\check-steam-wows-update.ps1 -Mode CheckAndBuild
powershell -ExecutionPolicy Bypass -File .\tools\run-wows-update-task.ps1 -Mode SelfTest
powershell -ExecutionPolicy Bypass -File .\tools\install-wows-update-task.ps1 -Mode Install
```

Run state is stored in the isolated worktree's Git-ignored `build\automation\wows-release-state.json`, with task logs in the adjacent `scheduled-logs` directory. Identical results notify only once. After publishing, provide the exact comment URL before manually running `MarkPublished`; the automation never guesses a URL or submits third-party content.

## Accuracy Notice

AP penetration uses unpacked AP shell parameters and an empirical formula to generate an approximate penetration table for fast in-battle checks. It is not an official pixel-perfect replay of the game ballistics system.

The armor database combines automatic extraction, geometry filtering, main-belt angle analysis, and manual correction rules. Complex layouts can still be wrong, especially segmented main belts, curved armor belts, turtleback armor, internal armor, turrets, local deck plates, underwater hit paths, and carrier side plating.

The current AP main-belt check only evaluates the target main belt. It does not model turtleback armor, inner armor layers, turrets, or complex underwater shell paths.

If you find a wrong result, please open an issue with:

- Ship name and game client language
- Shell type, gun caliber, and distance
- Target relative angle or screenshot
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
tools\                           # Build, install, database update, and main-belt analysis tools
dist\                            # Local release artifacts, not committed
```
