# APOvermatchAssistant Architecture

The in-battle visible panel is mounted by
`src/res_mods/PnFMods/ModsInstaller_4_3_1/mods/APOvermatchAssistant.xml`.
That XML patches `gui/battle_elements.xml` with a `lesta.unbound2.UbElement`
whose `elementName` is `OA_APOvermatchAssistant`. The element implementation
lives in `src/res_mods/gui/unbound2/PnFMods/APOvermatchAssistant.unbound`.

The package must not include a static `gui/battle_elements.xml`; Aslain and other
mods generate the live file, and `ModsInstaller_4_3_1` patches that current file
when the game starts.

The Python loader still enters through
`src/res_mods/PnFMods/APOvermatchAssistant/Main.py`. Keep that file focused on
game runtime integration:

- battle lifecycle registration
- lazy imports of WoWS runtime modules (`BigWorld`, `BWPersonality`, `ui`, `Vary`)
- current player, target, selected ammo, and camera access
- public loader functions (`init`, `start`, `stop`, `fini`, `kill`)

Pure helper modules live next to `Main.py` so the packaged mod can import them without
extra path setup:

- `overmatch_constants.py`: API metadata, stable constants, UI text, colors, and default payload shape.
- `overmatch_database.py`: armor database loading and vehicle-to-record lookup.
- `overmatch_rules.py`: shell rule limits, armor state calculation, and weapon display text.
- `overmatch_payload.py`: conversion from a target armor record plus a rule limit into the UI payload.
- `overmatch_utils.py`: defensive object access, numeric conversion, caliber normalization, and millimeter formatting.
- `overmatch_logging.py`: WoWS log bridge with console fallback.

The module boundary rule is: only `Main.py` should know about live WoWS objects.
Helper modules should accept plain dicts, numbers, and strings whenever possible.
This keeps the rules and payload behavior testable outside the game client.

The current unbound panel also reads battle data directly from `$datahub` for its
display state. Keep the display chain consistent with TTaro/PnF-style mods:

- install XML patches `battle_elements.xml`
- `OA_APOvermatchAssistant` is the mounted root element
- the root element owns target tracking and panel visibility
- row renderers only format already-selected display state

Generated armor data remains under `data/`. Do not hand-edit
`data/armor_overmatch.py` or the generated armor block in
`src/res_mods/gui/unbound2/PnFMods/APOvermatchAssistant.unbound`; use the generation
tools instead.

For Python-side changes, run the module tests with the local machine Python on
`PATH`:

```powershell
python .\tests\overmatch_python_module_tests.py
```

The unified test entrypoint is:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\test.ps1 -Build
```

The repository does not use a bundled or managed Python runtime. `tools\test.ps1`
uses `python` from `PATH`, or an explicit `-Python <path>` value. Use
`-SkipPython` only on machines that do not have Python installed. The repo-level
rule and package checks are:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\test-rule.ps1
powershell -ExecutionPolicy Bypass -File .\tools\build.ps1
```
