"""Angeles National tee rocks: one limestone marker per hole beside the back tee, like the real hole 1 rock
(logo disc, hole number, par, black/blue/white/red yardages). Writes props.csv and tee_rocks/TeeRock_NN.png (face decal)."""
import csv, math, os
from PIL import Image, ImageDraw, ImageFont
card = {int(r['hole']): r for r in csv.DictReader(open('scorecard.csv'))}
holes = {int(r['hole']): r for r in csv.DictReader(open('holes.csv'))}
tees = {int(r['hole']): r for r in csv.DictReader(open('tees.csv')) if r['box'] == '1'}
os.makedirs('tee_rocks', exist_ok=True)
fb, fr = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
F = lambda p, s: ImageFont.truetype(p, s) if os.path.exists(p) else ImageFont.load_default()
rows = []
for h in range(1, 19):
    t, g, c = tees[h], holes[h], card[h]
    tx, tz = float(t['x']), float(t['z']); dx, dz = float(g['green_x']) - tx, float(g['green_z']) - tz
    L = math.hypot(dx, dz); ux, uz = dx / L, dz / L
    x, z = tx - 4 * ux - 6 * uz, tz - 4 * uz + 6 * ux            # 4 m behind and 6 m left of the back tee
    yaw = (math.degrees(math.atan2(dx, dz)) + 180) % 360          # face turned back toward players walking up
    rows.append(dict(name="TeeRock_%02d" % h, type="tee_rock", x="%.2f" % x, z="%.2f" % z, y=t['y'], rot_y="%.0f" % yaw,
                     width_m=1.2, depth_m=0.6, height_m=1.0, colour="#D9D2C3",
                     note="hole %d par %s: black %s blue %s white %s red %s" % (h, c['par'], c['black'], c['blue'], c['white'], c['red'])))
    W, H = 1024, 768; im = Image.new('RGB', (W, H), (214, 207, 192)); d = ImageDraw.Draw(im)
    d.ellipse((W / 2 - 80, 40, W / 2 + 80, 200), fill=(95, 80, 55), outline=(60, 50, 35), width=6)
    d.text((W / 2, 120), "AN", font=F(fb, 70), fill=(200, 180, 120), anchor='mm')
    d.text((W / 2 - 120, 330), str(h), font=F(fb, 170), fill=(55, 50, 45), anchor='mm')
    d.text((W / 2 + 130, 300), "Par", font=F(fr, 80), fill=(55, 50, 45), anchor='mm')
    d.text((W / 2 + 130, 390), c['par'], font=F(fr, 80), fill=(55, 50, 45), anchor='mm')
    for i, (col, yd) in enumerate([((20, 20, 20), c['black']), ((40, 90, 200), c['blue']), ((245, 245, 245), c['white']), ((200, 30, 30), c['red'])]):
        cx, cy = W / 2 - 250 + (i % 2) * 330, 530 + (i // 2) * 120
        d.ellipse((cx - 18, cy - 18, cx + 18, cy + 18), fill=col, outline=(60, 60, 60), width=2)
        d.text((cx + 40, cy), yd, font=F(fb, 90), fill=(55, 50, 45), anchor='lm')
    im.save('tee_rocks/TeeRock_%02d.png' % h)
w = csv.DictWriter(open('props.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print("Wrote %d tee rocks to props.csv and tee_rocks/" % len(rows))
