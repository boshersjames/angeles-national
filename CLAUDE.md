# AngelesNational GSPro course

Real course rebuilt for GSPro (Unity 2018.2.8f1, OPCD). Toolkit: `../course-build` (the course-build repo). Read its
`README.md` once, then the skill for the element you are working on in `../course-build/skills/`. All thresholds come from
`../course-build/rules/*.json`; this course's overrides are in `course.json` under `rule_overrides`.

## Where things are
- `course.json`: frame, paths, GKD fields, tee slot map, overrides. Every script reads paths from here.
- Unity project: `C:\GSP\AngelesNational_Project`. Editor tools in `Assets\Editor\` are copies from `../course-build\unity\shared\`; sync with
  `../course-build\automation\Run-CourseAutomation.ps1 -SyncTools`.
- Automation output: `C:\GSP\AngelesNational_Project\AutomationOutput\latest.txt` then that folder's `summary.md` and `shots\`.
- Never change `C:\GSProV1\Core\GSP\Courses\` without backing up the GKD first.

## Driving Unity
- Unity closed: `../course-build\automation\Run-CourseAutomation.ps1 -Config automation\AngelesNational.json [-Steps "a,b"]`.
- Unity open: `../course-build\automation\Send-UnityCommand.ps1 <ping|run|shots|invoke|describe|menu|save|refresh>`.

## Process
Follow `course-build-gates`: one hole, one edit, photo pair each; control hole before/after on course-wide passes; back up
scene, terrain and GKD before every change. Run the LiDAR review (D1-D18) before the first gate and record answers in
`course_photos/decisions.csv`.

## Cost discipline
Measure with tools, not eyes. Colour: `colour_match.py`. Green edges: the edge survey. Pins: the pin-area test. Read the
summary a tool writes; open a render only when a number says something is wrong.

## This course
Split out of the moorpark repo (branch `claude/project-thread-47fcq5`, `courses/angeles_national`). `README.md` has the full data history.
- Frame: 2000 m square centred on 34.268109, -118.329107 (EPSG:6340, SW 376642.75 E, 3791683.25 N), y = elevation - 345 m,
  Unity Terrain 2000 x 187 x 2000. Ground 346.2 to 530.2 m (foothills N and E).
- Survey: USGS 3DEP `CA_LosAngeles_1_B23` (QL1, 2023-24), 38-45 pts/m2 on the course. Satellite NAIP 8192 px (0.24 m/px).
- `course.json` carries coursekit's keys beside the toolkit's; keep both in step. `paths.gkd` is `AngelesNational.GKD` at the
  repo root. `water_colour` (from BoJa's photos) is the lake colour; never tint water from the satellite.
- Habitat (wash and scrub) is a red penalty area, not OB; drop zones on 3, 6, 9, 18 (`local_rules.md`). Wood-chip free-drop
  beds are not drawn yet. Tee markers are limestone rocks with per-hole decals (`props.csv`, `tee_rocks/`).
- Open questions: hole 6 drop-zone carry is short; greens 1 and 3 over 3% tilt; hole 10 Black/Blue tees unmapped in OSM.
- Script order after `coursekit card`: `scripts/apply_checklist.py`, `fix_box_tees.py`, svg + `smooth_fairways.py` +
  `surrounds.py` + `teepads.py`, `svg_check.py`, `tee_levels.py`.
