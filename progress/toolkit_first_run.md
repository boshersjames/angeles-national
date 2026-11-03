# First headless toolkit run (2026-11-03)

Run from the course folder, course-build at 02dcbcb Skills: additive Tools section in all 23 (exact toolkit commands, rule keys, and 'no tool yet' gaps); no existing text changed.

## doctor.py

```
ok   course.json                            /home/user/angeles-national/course.json
ok   paths.toolkit                          /home/user/course-build
ok   heightmap size                         8396802 bytes (= 2049^2 x 2)
ok   gkd parses                             Angeles National Golf Club: 18 holes, 18 enabled
ok   svg greens match gkd                   21 outlines, 18 of 18 enabled holes matched
ok   paths.satellite                        /home/user/angeles-national/satellite.jpg
ok   paths.trees_csv                        /home/user/angeles-national/trees.csv
WARN paths.signs                            missing (/home/user/angeles-national/progress/hole_signs.json)
WARN paths.photos_root                      missing (/home/user/angeles-national/course_photos)
ok   python numpy                           
ok   python scipy                           
ok   python matplotlib                      
ok   python PIL                             
ok   python pyproj                          
ok   python laspy                           
ok   python pillow_heif                     
ok   tool git                               
ok   tool git-lfs                           
ok   tool ffmpeg                            
ok   tool yt-dlp                            
info unity_project                          C:/GSP/AngelesNational_Project not on this machine
info automation latest run                  none here

0 FAIL, 2 WARN
[exit 0]
```

## gkd_tools.py check

```
25 checks, 0 failing
[exit 0]
```

## green_report.py --smooth 0.6

```
# Green report (angeles_national, surface: course heightmap order 3, low-pass sigma 0.6 m)

Rules: pin area <= 1.7 deg over 17 points, pins >= 3 m from the edge, >= 4 valid areas >= 3 m apart; internal slope 1-3%.

| hole | area m2 | relief m | slope mean/p90 % | >3% | pins fail | pin angles | usable % | areas | flag | pass |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 500 | 1.04 | 5.2 / 9.7 | 73 | 4/4 | Thu:1.8 Fri:2.9 Sat:2.2 Sun:4.3 | 22 | 14 | steep >3% | FAIL |
| 2 | 524 | 0.65 | 3.3 / 5.7 | 51 | 2/4 | Thu:1.5 Fri:3.6 Sat:2.6 Sun:1.1 | 46 | 27 | steep >3% | FAIL |
| 3 | 665 | 1.78 | 5.0 / 10.8 | 54 | 1/4 | Thu:1.2 Fri:1.4 Sat:3.1 Sun:0.7 | 48 | 34 | steep >3% | FAIL |
| 4 | 600 | 0.77 | 3.7 / 6.0 | 57 | 3/4 | Thu:2.8 Fri:3.5 Sat:0.8 Sun:3.1 | 38 | 27 | steep >3% | FAIL |
| 5 | 454 | 0.61 | 3.2 / 5.3 | 48 | 1/4 | Thu:0.7 Fri:1.1 Sat:3.3 Sun:1.5 | 48 | 24 | steep >3% | FAIL |
| 6 | 789 | 1.82 | 4.7 / 9.1 | 57 | 2/4 | Thu:1.5 Fri:2.5 Sat:1.4 Sun:1.9 | 37 | 32 | steep >3% | FAIL |
| 7 | 690 | 1.12 | 4.1 / 7.9 | 59 | 4/4 | Thu:3.6 Fri:3.2 Sat:2.9 Sun:3.8 | 34 | 28 | steep >3% | FAIL |
| 8 | 504 | 0.93 | 3.8 / 7.4 | 54 | 3/4 | Thu:2.0 Fri:4.6 Sat:1.9 Sun:1.2 | 39 | 24 | steep >3% | FAIL |
| 9 | 651 | 0.85 | 3.2 / 5.9 | 38 | 0/4 | Thu:0.4 Fri:1.6 Sat:1.2 Sun:1.3 | 64 | 45 | steep >3% | PASS |
| 10 | 426 | 0.65 | 3.5 / 6.3 | 51 | 0/4 | Thu:0.8 Fri:1.3 Sat:1.3 Sun:1.2 | 54 | 24 | steep >3% | PASS |
| 11 | 352 | 0.64 | 3.5 / 5.5 | 54 | 1/4 | Thu:1.1 Fri:1.2 Sat:1.0 Sun:1.8 | 50 | 17 | steep >3% | FAIL |
| 12 | 462 | 0.94 | 5.6 / 10.9 | 70 | 4/4 | Thu:2.3 Fri:3.0 Sat:9.4 Sun:2.7 | 21 | 14 | steep >3% | FAIL |
| 13 | 507 | 0.87 | 4.1 / 7.6 | 55 | 1/4 | Thu:1.8 Fri:1.4 Sat:1.5 Sun:1.1 | 40 | 23 | steep >3% | FAIL |
| 14 | 514 | 1.13 | 4.5 / 8.1 | 68 | 2/4 | Thu:1.8 Fri:2.3 Sat:1.7 Sun:1.2 | 30 | 17 | steep >3% | FAIL |
| 15 | 513 | 0.57 | 2.6 / 4.8 | 28 | 0/4 | Thu:1.6 Fri:1.5 Sat:1.3 Sun:1.1 | 74 | 39 |  | PASS |
| 16 | 498 | 0.53 | 2.8 / 5.2 | 35 | 1/4 | Thu:1.2 Fri:1.8 Sat:1.2 Sun:1.6 | 61 | 33 |  | FAIL |
| 17 | 625 | 0.95 | 3.6 / 7.0 | 49 | 2/4 | Thu:2.4 Fri:1.5 Sat:1.5 Sun:2.9 | 36 | 29 | steep >3% | FAIL |
| 18 | 636 | 0.82 | 3.4 / 6.8 | 48 | 1/4 | Thu:1.6 Fri:0.9 Sat:1.0 Sun:4.4 | 46 | 35 | steep >3% | FAIL |
wrote progress/green_report
[exit 0]
```

## flyover_gate.py --end-fit --no-plots

```
no signs file at /home/user/angeles-national/progress/hole_signs.json: provisional sign spots from the back tees
hole  1: 508 frames  20.3 s (x1.00) yaw/1s 0.70 pitch/1s 4.50 | end pitch -28.6 (pin -28.6) h 14.2 m, 23.5 m short | terrain 14.1 m crown 4.2 m (tree 943, lift 0.0/0.0) | first: crown 4.2 sight 4.0 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 6.3 -> OK
hole  2: 667 frames  26.7 s (x1.00) yaw/1s 0.07 pitch/1s 4.50 | end pitch -29.6 (pin -29.6) h 15.3 m, 26.0 m short | terrain 15.2 m crown -1.4 m (tree 233, lift 0.0/0.0) | first: crown 1.7 sight 1.7 in-frame True | green 95% (cut off 0, pull-back 0.0) pin True sight 5.4 -> FAIL  [opening NOT fixed within 6 m (crown 1.7 m, sign sightline 1.7 m, sign in frame True, rise -1.4 m from crown of tree 233)]
hole  3: 317 frames  12.7 s (x1.00) yaw/1s 4.50 pitch/1s 2.20 | end pitch -9.4 (pin -9.4) h 16.2 m, 94.0 m short | terrain 16.2 m crown 1.6 m (tree 350, lift 0.0/0.0) | first: crown 3.2 sight 3.3 in-frame True | green 70% (cut off 25, pull-back 9.5) pin True sight 5.4 -> FAIL  [opening moved 2.8 m (back 4.5 -> 2.5, side 1.6 -> -0.4): rise through crown of tree 350 (0.5 m)]
hole  4: 524 frames  21.0 s (x1.00) yaw/1s 0.67 pitch/1s 4.50 | end pitch -29.1 (pin -29.1) h 16.3 m, 28.0 m short | terrain 16.2 m crown 1.5 m (tree 428, lift 0.0/0.0) | first: crown 1.7 sight 1.8 in-frame True | green 98% (cut off 0, pull-back 0.0) pin True sight 6.8 -> OK  [opening moved 2.0 m (back 4.5 -> 2.5, side 1.6 -> 1.6): camera in crown of tree 776]
hole  5: 521 frames  20.8 s (x1.00) yaw/1s 0.01 pitch/1s 4.50 | end pitch -28.8 (pin -28.8) h 16.3 m, 28.0 m short | terrain 16.3 m crown 2.9 m (tree 1062, lift 0.0/0.0) | first: crown 2.9 sight 3.0 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 7.3 -> OK
hole  6: 550 frames  22.0 s (x1.00) yaw/1s 0.60 pitch/1s 4.50 | end pitch -28.7 (pin -28.7) h 16.2 m, 28.5 m short | terrain 16.1 m crown -0.3 m (tree 676, lift 0.0/0.0) | first: crown 0.1 sight 0.1 in-frame True | green 96% (cut off 0, pull-back 0.0) pin True sight 4.5 -> FAIL  [opening NOT fixed within 6 m (crown 0.1 m, sign sightline 0.1 m, sign in frame True, rise -0.3 m from crown of tree 676)]
hole  7: 317 frames  12.7 s (x1.00) yaw/1s 4.50 pitch/1s 3.83 | end pitch -12.1 (pin -12.1) h 16.1 m, 76.0 m short | terrain 16.1 m crown 2.4 m (tree 1071, lift 0.0/0.0) | first: crown 2.8 sight 2.9 in-frame True | green 69% (cut off 30, pull-back 8.0) pin True sight 8.2 -> FAIL
hole  8: 617 frames  24.7 s (x1.00) yaw/1s 0.24 pitch/1s 4.50 | end pitch -29.0 (pin -29.0) h 14.1 m, 23.5 m short | terrain 14.0 m crown 2.0 m (tree 1061, lift 0.0/0.0) | first: crown 2.1 sight 0.9 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 6.9 -> OK
hole  9: 571 frames  22.8 s (x1.00) yaw/1s 0.10 pitch/1s 4.50 | end pitch -29.1 (pin -29.1) h 16.4 m, 28.0 m short | terrain 16.4 m crown 0.6 m (tree 624, lift 0.0/0.0) | first: crown 1.9 sight 1.4 in-frame True | green 92% (cut off 0, pull-back 0.0) pin True sight 9.1 -> FAIL  [opening NOT fixed within 6 m (crown 1.9 m, sign sightline 1.4 m, sign in frame True, rise 0.6 m from crown of tree 624)]
hole 10: 543 frames  21.7 s (x1.00) yaw/1s 1.02 pitch/1s 4.50 | end pitch -30.9 (pin -30.9) h 13.7 m, 23.0 m short | terrain 13.6 m crown -1.4 m (tree 211, lift 0.0/0.0) | first: crown 2.9 sight 2.5 in-frame True | green 97% (cut off 0, pull-back 0.0) pin True sight 6.7 -> FAIL  [opening NOT fixed within 6 m (crown 2.9 m, sign sightline 2.5 m, sign in frame True, rise -1.5 m from crown of tree 211)]
hole 11: 428 frames  17.1 s (x1.00) yaw/1s 1.34 pitch/1s 4.50 | end pitch -29.2 (pin -29.2) h 14.4 m, 23.5 m short | terrain 14.4 m crown 1.8 m (tree 467, lift 0.0/0.0) | first: crown 2.1 sight 1.9 in-frame True | green 98% (cut off 0, pull-back 0.0) pin True sight 3.9 -> OK  [opening moved 2.0 m (back 4.5 -> 2.5, side 1.6 -> 1.6): camera in crown of tree 467]
hole 12: 317 frames  12.7 s (x1.00) yaw/1s 4.50 pitch/1s 4.31 | end pitch -19.1 (pin -19.1) h 16.2 m, 49.0 m short | terrain 16.1 m crown 1.7 m (tree 474, lift 0.0/0.0) | first: crown 2.4 sight 2.5 in-frame True | green 77% (cut off 19, pull-back 3.0) pin True sight 4.0 -> FAIL
hole 13: 592 frames  23.7 s (x1.00) yaw/1s 4.40 pitch/1s 4.50 | end pitch -33.3 (pin -33.3) h 13.8 m, 23.5 m short | terrain 13.6 m crown 2.0 m (tree 909, lift 0.0/0.0) | first: crown 2.1 sight 2.2 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 3.3 -> OK
hole 14: 331 frames  13.2 s (x1.00) yaw/1s 4.50 pitch/1s 4.22 | end pitch -24.4 (pin -24.4) h 16.0 m, 37.5 m short | terrain 16.0 m crown 1.9 m (tree 163, lift 0.0/0.0) | first: crown 3.7 sight 2.3 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 5.0 -> OK
hole 15: 562 frames  22.5 s (x1.00) yaw/1s 0.09 pitch/1s 4.50 | end pitch -28.7 (pin -28.7) h 17.0 m, 30.0 m short | terrain 16.4 m crown -0.1 m (tree 597, lift 0.0/0.0) | first: crown 1.0 sight 0.3 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 5.3 -> FAIL  [opening NOT fixed within 6 m (crown 1.0 m, sign sightline 0.3 m, sign in frame True, rise -0.1 m from crown of tree 597)]
hole 16: 622 frames  24.9 s (x1.00) yaw/1s 0.77 pitch/1s 4.50 | end pitch -29.4 (pin -29.4) h 15.0 m, 25.0 m short | terrain 15.0 m crown 5.1 m (tree 1005, lift 0.0/0.0) | first: crown 5.1 sight 4.6 in-frame True | green 100% (cut off 0, pull-back 0.0) pin True sight 6.8 -> OK
hole 17: 490 frames  19.6 s (x1.00) yaw/1s 4.50 pitch/1s 4.50 | end pitch -30.1 (pin -30.1) h 15.6 m, 26.5 m short | terrain 15.6 m crown 4.5 m (tree 606, lift 0.0/0.0) | first: crown 5.0 sight 4.0 in-frame True | green 95% (cut off 0, pull-back 0.0) pin True sight 2.6 -> OK
hole 18: 516 frames  20.6 s (x1.00) yaw/1s 1.99 pitch/1s 4.50 | end pitch -28.6 (pin -28.6) h 16.5 m, 28.5 m short | terrain 16.5 m crown 0.7 m (tree 463, lift 0.0/0.0) | first: crown 0.9 sight 0.6 in-frame True | green 97% (cut off 0, pull-back 0.0) pin True sight 6.3 -> FAIL  [opening NOT fixed within 6 m (crown 0.9 m, sign sightline 0.6 m, sign in frame True, rise 0.7 m from crown of tree 463)]
Failed holes: 2, 3, 6, 7, 9, 10, 12, 15, 18

Poster frames (first / rise / mid / approach / end) per hole are in flyover_gate.json; shots for the PC render in flyover_shots.json (8993 frames).
[exit 1]
```

## gate_report.py

```
# Gate report: angeles_national (18 holes)

Sources: flyover, lidar-proxy. Missing: Unity CourseGreenChecks (checks/greens_all18.csv): run Course Checks > Greens on the PC.

GKD checks: all pass

| hole | source | step cm | lip cm | col dy | tiers | crown m | pins fail | usable % | areas | fall dir | flyover | result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | lidar-proxy+flyover | - | - | - | - | - | 2 | 46 | 27 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 3 | lidar-proxy+flyover | - | - | - | - | - | 1 | 48 | 34 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 6 | lidar-proxy+flyover | - | - | - | - | - | 2 | 37 | 32 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 7 | lidar-proxy+flyover | - | - | - | - | - | 4 | 34 | 28 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 9 | lidar-proxy+flyover | - | - | - | - | - | 0 | 64 | 45 | - | FAIL | **FAIL** flyover |
| 10 | lidar-proxy+flyover | - | - | - | - | - | 0 | 54 | 24 | - | FAIL | **FAIL** flyover |
| 12 | lidar-proxy+flyover | - | - | - | - | - | 4 | 21 | 14 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 15 | lidar-proxy+flyover | - | - | - | - | - | 0 | 74 | 39 | - | FAIL | **FAIL** flyover |
| 18 | lidar-proxy+flyover | - | - | - | - | - | 1 | 46 | 35 | - | FAIL | **FAIL** flyover warn: pins(lidar) |
| 1 | lidar-proxy+flyover | - | - | - | - | - | 4 | 22 | 14 | - | PASS | PASS warn: pins(lidar) |
| 4 | lidar-proxy+flyover | - | - | - | - | - | 3 | 38 | 27 | - | PASS | PASS warn: pins(lidar) |
| 5 | lidar-proxy+flyover | - | - | - | - | - | 1 | 48 | 24 | - | PASS | PASS warn: pins(lidar) |
| 8 | lidar-proxy+flyover | - | - | - | - | - | 3 | 39 | 24 | - | PASS | PASS warn: pins(lidar) |
| 11 | lidar-proxy+flyover | - | - | - | - | - | 1 | 50 | 17 | - | PASS | PASS warn: pins(lidar) |
| 13 | lidar-proxy+flyover | - | - | - | - | - | 1 | 40 | 23 | - | PASS | PASS warn: pins(lidar) |
| 14 | lidar-proxy+flyover | - | - | - | - | - | 2 | 30 | 17 | - | PASS | PASS warn: pins(lidar) |
| 16 | lidar-proxy+flyover | - | - | - | - | - | 1 | 61 | 33 | - | PASS | PASS warn: pins(lidar) |
| 17 | lidar-proxy+flyover | - | - | - | - | - | 2 | 36 | 29 | - | PASS | PASS warn: pins(lidar) |
wrote progress/gate_report
[exit 1]
```
