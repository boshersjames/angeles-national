# Flyover gate (data pass)

Inputs: GKD `AngelesNational.GKD`, signs `progress/hole_signs.json`, trees `trees.csv`, greens `course.svg`, heightmap `heightmap_2049.raw`, pin index 0.

Pass = yaw and pitch under 5 deg in every 1 s window, opening camera clear of crowns with the sign in frame and unhidden, terrain clearance 5 m+, crown clearance 1.5 m+ on the whole path, no part of the green cut off ahead or to the side in the end frame (the part under the camera is reported, not failed), pin in frame and not behind a crown.

| Hole | s | yaw/1s | pitch/1s | end pitch (target) | end h / short (used) | terrain min (after rise) | crown min (tree, frame), lift rise/flight | first: crown / sight / in frame | green: in / under cam / cut off (pull-back to fit) | pin | result | opening move |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 20.3 | 0.7 | 4.5 | -28.6 (-28.6) | 14.2 / 23.5 | 14.1 | 4.2 (943, f0), 0.0 / 0.0 | 4.2 / 4.0 / yes | 100% / 0 / 0 (0 m) | in, sight 6.3 | **OK** |  |
| 2 | 26.7 | 0.1 | 4.5 | -29.6 (-29.6) | 15.3 / 26.0 | 15.2 | -1.4 (233, f54), 0.0 / 0.0 | 1.7 / 1.7 / yes | 95% / 4 / 0 (0 m) | in, sight 5.4 | **FAIL** | opening NOT fixed within 6 m (crown 1.7 m, sign sightline 1.7 m, sign in frame True, rise -1.4 m from crown of tree 233) |
| 3 | 12.7 | 4.5 | 2.2 | -9.4 (-9.4) | 16.2 / 94.0 | 16.2 | 1.6 (350, f52), 0.0 / 0.0 | 3.2 / 3.3 / yes | 70% / 0 / 25 (10 m) | in, sight 5.4 | **FAIL** | opening moved 2.8 m (back 4.5 -> 2.5, side 1.6 -> -0.4): rise through crown of tree 350 (0.5 m) |
| 4 | 21.0 | 0.7 | 4.5 | -29.1 (-29.1) | 16.3 / 28.0 | 16.2 | 1.5 (428, f50), 0.0 / 0.0 | 1.7 / 1.8 / yes | 98% / 2 / 0 (0 m) | in, sight 6.8 | **OK** | opening moved 2.0 m (back 4.5 -> 2.5, side 1.6 -> 1.6): camera in crown of tree 776 |
| 5 | 20.8 | 0.0 | 4.5 | -28.8 (-28.8) | 16.3 / 28.0 | 16.3 | 2.9 (1062, f0), 0.0 / 0.0 | 2.9 / 3.0 / yes | 100% / 0 / 0 (0 m) | in, sight 7.3 | **OK** |  |
| 6 | 22.0 | 0.6 | 4.5 | -28.7 (-28.7) | 16.2 / 28.5 | 16.1 | -0.3 (676, f40), 0.0 / 0.0 | 0.1 / 0.1 / yes | 96% / 4 / 0 (0 m) | in, sight 4.5 | **FAIL** | opening NOT fixed within 6 m (crown 0.1 m, sign sightline 0.1 m, sign in frame True, rise -0.3 m from crown of tree 676) |
| 7 | 12.7 | 4.5 | 3.8 | -12.1 (-12.1) | 16.1 / 76.0 | 16.1 | 2.4 (1071, f44), 0.0 / 0.0 | 2.8 / 2.9 / yes | 69% / 0 / 30 (8 m) | in, sight 8.2 | **FAIL** |  |
| 8 | 24.7 | 0.2 | 4.5 | -29.0 (-29.0) | 14.1 / 23.5 | 14.0 | 2.0 (1061, f40), 0.0 / 0.0 | 2.1 / 0.9 / yes | 100% / 0 / 0 (0 m) | in, sight 6.9 | **OK** |  |
| 9 | 22.8 | 0.1 | 4.5 | -29.1 (-29.1) | 16.4 / 28.0 | 16.4 | 0.6 (624, f58), 0.0 / 0.0 | 1.9 / 1.4 / yes | 92% / 7 / 0 (0 m) | in, sight 9.1 | **FAIL** | opening NOT fixed within 6 m (crown 1.9 m, sign sightline 1.4 m, sign in frame True, rise 0.6 m from crown of tree 624) |
| 10 | 21.7 | 1.0 | 4.5 | -30.9 (-30.9) | 13.7 / 23.0 | 13.6 | -1.4 (211, f58), 0.0 / 0.0 | 2.9 / 2.5 / yes | 97% / 2 / 0 (0 m) | in, sight 6.7 | **FAIL** | opening NOT fixed within 6 m (crown 2.9 m, sign sightline 2.5 m, sign in frame True, rise -1.5 m from crown of tree 211) |
| 11 | 17.1 | 1.3 | 4.5 | -29.2 (-29.2) | 14.4 / 23.5 | 14.4 | 1.8 (467, f44), 0.0 / 0.0 | 2.1 / 1.9 / yes | 98% / 1 / 0 (0 m) | in, sight 3.9 | **OK** | opening moved 2.0 m (back 4.5 -> 2.5, side 1.6 -> 1.6): camera in crown of tree 467 |
| 12 | 12.7 | 4.5 | 4.3 | -19.1 (-19.1) | 16.2 / 49.0 | 16.1 | 1.7 (474, f46), 0.0 / 0.0 | 2.4 / 2.5 / yes | 77% / 0 / 19 (3 m) | in, sight 4.0 | **FAIL** |  |
| 13 | 23.7 | 4.4 | 4.5 | -33.3 (-33.3) | 13.8 / 23.5 | 13.6 | 2.0 (909, f36), 0.0 / 0.0 | 2.1 / 2.2 / yes | 100% / 0 / 0 (0 m) | in, sight 3.3 | **OK** |  |
| 14 | 13.2 | 4.5 | 4.2 | -24.4 (-24.4) | 16.0 / 37.5 | 16.0 | 1.9 (163, f54), 0.0 / 0.0 | 3.7 / 2.3 / yes | 100% / 0 / 0 (0 m) | in, sight 5.0 | **OK** |  |
| 15 | 22.5 | 0.1 | 4.5 | -28.7 (-28.7) | 17.0 / 30.0 | 16.4 | -0.1 (597, f48), 0.0 / 0.0 | 1.0 / 0.3 / yes | 100% / 0 / 0 (0 m) | in, sight 5.3 | **FAIL** | opening NOT fixed within 6 m (crown 1.0 m, sign sightline 0.3 m, sign in frame True, rise -0.1 m from crown of tree 597) |
| 16 | 24.9 | 0.8 | 4.5 | -29.4 (-29.4) | 15.0 / 25.0 | 15.0 | 5.1 (1005, f0), 0.0 / 0.0 | 5.1 / 4.6 / yes | 100% / 0 / 0 (0 m) | in, sight 6.8 | **OK** |  |
| 17 | 19.6 | 4.5 | 4.5 | -30.1 (-30.1) | 15.6 / 26.5 | 15.6 | 4.5 (606, f48), 0.0 / 0.0 | 5.0 / 4.0 / yes | 95% / 4 / 0 (0 m) | in, sight 2.6 | **OK** |  |
| 18 | 20.6 | 2.0 | 4.5 | -28.6 (-28.6) | 16.5 / 28.5 | 16.5 | 0.7 (463, f48), 0.0 / 0.0 | 0.9 / 0.6 / yes | 97% / 2 / 0 (0 m) | in, sight 6.3 | **FAIL** | opening NOT fixed within 6 m (crown 0.9 m, sign sightline 0.6 m, sign in frame True, rise 0.7 m from crown of tree 463) |

End spot: 12 m short of the pin, 8 m over the ground (v4 default 12 / 8), pulled back per hole until the green fits (--end-fit).

Failed holes: 2, 3, 6, 7, 9, 10, 12, 15, 18

Poster frames (first / rise / mid / approach / end) per hole are in flyover_gate.json; shots for the PC render in flyover_shots.json (8993 frames).
