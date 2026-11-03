# Angeles National Golf Club (GSPro build)

Angeles National Golf Club, 9500 Sunland Blvd, Sunland (Los Angeles County). 18 holes, par 72, Nicklaus Design (opened 2004), laid out in the Big Tujunga Wash below the San Gabriel foothills. Built with `coursekit.py`.

## Frame
- 2000 m square centred on the middle of the mapped golf features (34.26810945, -118.3291071); the course is 1470 m east-west by 1054 m north-south, so there is 250-470 m of margin all round. James's pin (34.268052, -118.334466) is inside, 500 m west of centre. EPSG:6340, SW corner in `course.json`.
- Unity x = metres east, z = metres north, y = elevation - 345 m.
- `heightmap_2049.raw` (plain git, not LFS, via this folder's .gitattributes; same for map.osm, the masks and the tee-rock decals. Only satellite.jpg is LFS, pushed from the Mac): 2049 x 2049, 16-bit, Windows byte order. Unity Terrain 2000 x 187 x 2000 (0.98 m per sample). Ground 346.2 to 530.2 m (the high ground is the foothills to the north and east).

## LiDAR
USGS 3DEP `CA_LosAngeles_1_B23` (QL1, 2023-24). Sampled 100 m squares on the course: 38 to 45 points/m2 (11 to 25 ground points/m2), about 8-10x Tierra Rejada (2018, ~4-5/m2) and double Hansen Dam. Classes are 1 unclassified, 2 ground, 17 bridge (I-210), so trees and brush come from height above ground.

    python ../../coursekit.py lidar --ept CA_LosAngeles_1_B23

`points.npz` (1.1 GB) is not in git.

## Satellite
`satellite.jpg`: NAIP via imagery.nationalmap.gov, 8192 px (0.24 m/px), fetched on the Mac (blocked from the cloud). In Unity: Max Size 8192, Terrain Size 2000.

## Holes (`holes.csv`, `tees.csv`)
`map.osm` from James (OSM export, 2026-10-28; in the project files under angeles-national/, not in git): 18 hole lines with refs and pars, 60 tees, 21 greens (incl. practice), 55 bunkers, 15 fairways, 3 water hazards, 16 penalty areas, range, 46 cart paths.
Dropped three back tees that don't match the card: hole 4 box 1 (529 yd vs card Black 427) and hole 8 boxes 1-2 (621/608 vs 530). Hole 10's Black/Blue tees (459/429) aren't mapped; OSM's back tee gives 425.

## Scorecard (`scorecard.csv`, from the club card)
Par 4 5 3 4 4 4 3 5 4 | 4 4 3 5 3 4 5 4 4 = 72.
Black 7141 (74.7/143), Blue 6597 (72.1/136), White 6169 (70.0/130), Red 4899 (68.9/116). Men's and women's handicaps in the file.

## Local rules (`local_rules.md`)
Habitat = red penalty area (no entry); wood chip beds = free drop; drop areas past the arroyos on 3, 6, 9 and 18.

## Tee rocks (`props.csv`, `tee_rocks/`)
The real tee markers are limestone boulders with the logo disc, hole number, par and four dotted yardages. `tee_rocks.py` writes one per hole beside the back tee (4 m behind, 6 m left, facing players walking up) and a 1024x768 face decal per hole from the card (`tee_rocks/`).

## Trees and brush
`trees.csv`: 936 LiDAR trees (>= 3 m) near the holes after the OSM and satellite filters (151 grey/tan crowns dropped).
`shrubs.csv` / `brush_mask.png`: 18.5 ha of LiDAR brush (0.5-3.5 m), 7,193 shrubs.

## Vegetation (`coursekit vegetation --wash 0.35`)
New `--wash` option for river-wash courses: pale sand/cobble ground is the wash floor (habitat), not unmapped trails. Without it the whole wash between the holes was dropped as "trail" and left bare.
- `terrain_masks/wash_sand_cobble.mask`: the wash floor (paint pale sand + river cobble texture).
- `brush_sage_scrub.mask`: full strength on the banks, half strength on the wash floor (sparse sage/buckwheat).
- `grass_dry_hillside.mask` (golden grass, banks only, never on the wash), `grass_deep_rough.mask` (band next to turf), `no_grass.mask`.
- `shrubs_clean.csv`: 5,067 LiDAR shrubs + 4,117 edge-row shrubs; `shrubs_removed.csv`: 2,126 with reasons.
- A little false "wash" lands on the I-210 south of the course (outside the OSM export); it is far from play.
Masks and previews are in the project files (angeles-national/).

## Course drawing (`course.svg`, draft)
`python ../../coursekit.py svg --smooth 12 --min-green 0.355 --fw-corridor 45`: greens, tees, 48 bunker shapes and 3 lakes from OSM, 5.4 ha of OSM fairway plus 6.3 ha traced from the photo (OSM maps only 15 fairways; the defaults found 0.5 ha because the turf here is dry and striped), 1.5 m collar round every green (no uphill banks found). Rough 21 ha, deep rough 3.3 ha; wash and scrub are left out of the rough mesh. Preview `course_svg_preview.png` (project files). Check the fairway edges in Inkscape, especially the hole by the small lake.

## Look (from James's photos, project files angeles-national/reference/)
- Off the turf is the open wash, not hillside grass: pale sand and river cobbles with low sage scrub, red-brown buckwheat, yucca, scattered oaks/sycamores. Golden grass only on the backdrop hills.
- Dark red-brown mulch beds beside the paths (the wood-chip free-drop areas); wooden bridges over the arroyos; palms round the 18th lake.
- Big kidney bunkers, mown collar round every green.

## Cart paths (`cartpaths.csv`, 46 paths, 9.3 km) - not like Tierra
Tierra's paths were washed-out pure white with ragged edges. Here:
- `coursekit osm` now rounds every OSM path (3 Chaikin passes, ends kept) and resamples it every 1 m, so the strips follow smooth curves instead of a few straight legs.
- No path crosses a green, tee, bunker or fairway; the closest to a green is 2.7 m (practice green by the clubhouse).
- Material: mid-grey, matte, broom-finished concrete with joints and tyre tracks (Course Look > Cart Paths), never bright white. Paths by the clubhouse are red-brown coloured concrete.

## Tierra lessons to apply in the build
- **Collar:** `svg --collar` puts a 1.5 m fairway-grass ring round every green (uphill banks keep rough).
- **Bunkers:** each OSM bunker its own Bunker-layer shape; shallow with flat floors (Lower Terrain Under Meshes 1 m), Sand Raked Dirt Lip Thin + sand physics; test a ball into a greenside and a fairway bunker before publishing.

## Greenkeeper file (`AngelesNational.GKD`, draft)
    python ../../coursekit.py card --template <Harding.GKD> --name "Angeles National Golf Club" --scene AngelesNational --line-tees --ob --habitat-penalty --drop-holes 3,6,9,18
- Tees: Black/Blue/White/Red from `card.csv` (the club card); every card yardage matched a mapped tee box (forward tees on 1, 3, 8, 10, 17, 18 placed on the hole line at the card yardage). Ratings Black 74.7/143, Blue 72.1/136, White 70.0/130, Red 68.9/116.
- Aim points at the widest part of the fairway on 14 holes; 4 pins per green.
- New `--habitat-penalty`: the wash and scrub inside the course are red penalty areas ("No entry into habitat"), not interior OB. In-bounds is turf plus 3 m beside it and the cart paths; homes, yards and roads stay OB. Big habitat patches get a slit cut out to each hole they wrap round so the single-ring GKD polygon doesn't cover the hole.
- New `--drop-holes 3,6,9,18`: the first habitat each hole line crosses is cut out as its own penalty area with a drop zone 6 m past it on in-bounds ground (GSPro allows one drop zone per hazard). Carries: 3 = 34-124 m off the back tee, 6 = 17-27 m, 9 = 323-382 m (in front of the green), 18 = 121-138 m. Check 6 in Greenkeeper; its carry is short.
- Wood-chip beds (free drop) are not drawn yet: they aren't in OSM.
- Preview `ob_preview.png` (project files).

## BoJa checklist pass (10/28, /mnt/project-files/course-build/BOJA_FEEDBACK_CHECKLIST.md)
Rebuilt with Hansen Dam's coursekit fixes merged in. Scripts are in `scripts/`, run from this folder in this order:
1. `coursekit trees --min-green 0`: all 1,087 LiDAR trees kept (no satellite colour drop), then `scripts/clear_bunker_crowns.py`: 29 trees moved or shrunk so 1.3 x crown + 0.5 m clears every bunker (none left touching sand).
2. `coursekit svg --smooth 12 --min-green 0.355 --fw-corridor 45` (collars 3 m sides / 5 m back, deep rough 6 m off greens), `scripts/smooth_fairways.py` (11.3 ha fairway), `scripts/surrounds.py` (`bunkers.csv` depth/face plan; no fairway/rough/deep over sand; 751 m2 of collar dropped on uphill banks).
3. `coursekit card ... --line-tees --ob --habitat-penalty --drop-holes 3,6,9,18` (see above), then `scripts/apply_checklist.py`: par-3 aims at the green (3, 7, 12, 14); tees at least 3 m off cart paths (13 Black slid 2 m sideways); drop-zone areas innerOOB=false, noAIL=true, freeDrop=false; DefaultStimp 2 / MaxStimp 5 / green firmness 0 / fairway 0 (approved: stimp 10, Normal, moderate); Designer jboshers (BoJa's choice for every course), Desert keyword, altitude 1230 ft; `checks/green_slopes.csv`.
4. `scripts/teepads.py`: 19 card-placed tees get a flat 9 x 7 m pad with a 2 m first cut. `scripts/svg_check.py`: all 72 tees sit 1.5 m+ inside a Tee shape, none in a fairway notch; none in a hazard; none within 3 m of a path.
- Green slopes over 3% (plane fit from the heightmap): hole 1 (3.9%) and hole 3 (4.4%). The p90 local-slope column flags nearly every green at 1 m sampling; treat it as noise until the 0.5 m green meshes are built.

## For the Unity build on the PC
- Own project `C:\GSP\AngelesNational_Project`. Terrain 2000 x 187 x 2000, heightmap 2049 RAW 16-bit Windows, y = elevation - 345 m. Satellite 8192 px over 2000 m (import at 4096 per the checklist).
- Paint `wash_sand_cobble.mask` with a pale sand + river-cobble layer (the habitat floor); `brush_sage_scrub.mask` is half strength on the wash (sparse sage/buckwheat, yucca), full on the banks; golden grass only on the banks. Habitat plays as a red penalty area, not OB.
- Cart paths: mid-grey matte broom-finished concrete with joints, lifted 4 cm, never bright white; red-brown near the clubhouse.
- Tee rocks: `props.csv` (type tee_rock, 1.2 x 0.6 x 1.0 m limestone boulder) with `tee_rocks/TeeRock_NN.png` on the face.
- Shot tests to run first: greenside and fairway bunker (ball stays in, needs loft), chip from the collar, ball into the habitat (penalty-area drop options), drop zones on 3, 6, 9, 18.

## PC build fixes (10/29)
- `scripts/fix_box_tees.py` (from Wilson, plus Red, a 3 m reach and the 3 m cart-path rule): every tee within 3 m of a mapped box now sits 1.6 m+ inside it, so no 9x7 pad merges with a box into a jagged shape that OPCD drops (8 White, 13 Black/White, 14 Black were on rough/deep rough). 22 tees moved, yardages within a few yards of the card. `teepads.py` now pads only tees not 1.2 m inside a tee shape: 6 Red pads, none touching a box.
- `scripts/tee_levels.py`: each tee's GKD y = mean ground over its whole tee shape, since the build levels the shape (7 Blue was 0.70 m high, 7 Black 0.79 m). Also flags any pad merged with a box (none).
- Water colour: the NAIP photo shows the lakes near-black teal (44, 68, 63), which is why the 18th lake renders dark. From BoJa's photos the lake is deep blue #26487D with shallow edges #406785 (`course.json` water_colour). Set the water material colour from these, not from the satellite.
- Order after `card`: apply_checklist.py, fix_box_tees.py AngelesNational.GKD heightmap_2049.raw, svg + smooth_fairways + surrounds + teepads, svg_check, tee_levels.
