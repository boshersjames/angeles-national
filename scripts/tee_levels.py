"""Check every GKD tee against course.svg and set its height to the level its tee mesh will get.
OPCD/the PC build flattens each tee shape, so a tee's GKD y must be the mean ground over the whole shape, not the
ground under the point (7 Blue sat 0.73 m above its mesh). Also reports pads that touch a mapped box (they merge into
one jagged shape that OPCD drops). Run in the course folder after teepads.py."""
import json, re, xml.etree.ElementTree as ET
import numpy as np
from pyproj import Transformer
from shapely.geometry import Polygon, Point
from shapely.ops import unary_union
c = json.load(open("course.json")); S = c["size"]
svg = open("course.svg").read()
i = svg.find('inkscape:label="Tee"'); blk = svg[i:svg.find("</g>", i)]
shapes = []
for d_ in re.findall(r' d="([^"]+)"', blk):
    for sp in re.split(r"(?=M )", d_.strip()):
        n = [float(v) for v in re.findall(r"-?\d+\.?\d*", sp)]
        pts = [(n[k], S - n[k + 1]) for k in range(0, len(n) - 1, 2)]
        if len(pts) > 2: shapes.append(Polygon(pts).buffer(0))
merged = unary_union(shapes); merged = list(merged.geoms) if hasattr(merged, "geoms") else [merged]
t = Transformer.from_crs("EPSG:4326", "EPSG:%d" % c["epsg"], always_xy=True)
r = ET.parse("map.osm").getroot(); N = {}
for nd in r.iter("node"):
    e, nn = t.transform(float(nd.get("lon")), float(nd.get("lat"))); N[nd.get("id")] = (e - c["sw_e"], nn - c["sw_n"])
boxes = [Polygon([N[q.get("ref")] for q in w.findall("nd")]).buffer(0) for w in r.iter("way")
         if any(q.get("k") == "golf" and q.get("v") == "tee" for q in w.findall("tag"))]
pads = [p for p in re.findall(r'<path id="tee_\d+"', svg)]
H = np.fromfile("heightmap_2049.raw", "<u2").reshape(2049, 2049) * c["terrain_height"] / 65535
def mean_ground(poly):
    x0, z0, x1, z1 = poly.bounds
    v = [H[int(round(z * 2048 / S)), int(round(x * 2048 / S))] for x in np.arange(x0, x1, 0.5) for z in np.arange(z0, z1, 0.5) if poly.contains(Point(x, z))]
    return float(np.mean(v))
d = json.load(open("AngelesNational.GKD")); bad = []; moved = []
for h in d["Holes"]:
    for tee in h["Tees"]:
        if tee["TeeType"] not in ("Black", "Blue", "White", "Red") or not tee["Position"]:
            continue
        p = Point(tee["Position"]["x"], tee["Position"]["z"])
        sh = [m for m in merged if m.contains(p)]
        if not sh or sh[0].exterior.distance(p) < 1.2:
            bad.append("%d %s off or near the edge of its tee shape" % (h["HoleNumber"], tee["TeeType"])); continue
        boxes_in = [b for b in boxes if b.intersects(sh[0])]
        if len(boxes_in) == 1 and sh[0].area > boxes_in[0].area * 1.15:
            bad.append("%d %s: its tee shape is a mapped box with a pad merged on" % (h["HoleNumber"], tee["TeeType"]))
        y = round(mean_ground(sh[0]), 3)
        if abs(y - tee["Position"]["y"]) > 0.05:
            moved.append("%d %s %.2f m" % (h["HoleNumber"], tee["TeeType"], y - tee["Position"]["y"]))
        tee["Position"]["y"] = y
json.dump(d, open("AngelesNational.GKD", "w", encoding="utf-8"), indent=1)
print("tee y set to the mean ground of its tee shape:", ", ".join(moved) or "none changed")
print("problems:", bad or "none")
