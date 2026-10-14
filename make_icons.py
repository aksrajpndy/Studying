"""Draws the StudyRing bell icon into the Android project's mipmap folders."""
import os
from PIL import Image, ImageDraw

BLUE = (35, 69, 240, 255)
WHITE = (255, 255, 255, 255)
RES = os.path.join("android", "app", "src", "main", "res")
DENSITIES = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}


def bell(size, scale, background=None, circle=False):
    """Bell centred on a size x size canvas. scale = bell height as a share of the canvas."""
    ss = 4  # supersample for smooth edges
    s = size * ss
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if background:
        if circle:
            d.ellipse([0, 0, s - 1, s - 1], fill=background)
        else:
            d.rectangle([0, 0, s, s], fill=background)
    h = s * scale
    w = h * 0.86
    cx = s / 2
    top = (s - h) / 2
    # dome, body, rim, clapper, handle
    d.ellipse([cx - w * 0.34, top + h * 0.10, cx + w * 0.34, top + h * 0.10 + w * 0.68], fill=WHITE)
    d.polygon([(cx - w * 0.34, top + h * 0.10 + w * 0.34), (cx + w * 0.34, top + h * 0.10 + w * 0.34),
               (cx + w * 0.50, top + h * 0.74), (cx - w * 0.50, top + h * 0.74)], fill=WHITE)
    d.rounded_rectangle([cx - w * 0.56, top + h * 0.70, cx + w * 0.56, top + h * 0.80], radius=h * 0.05, fill=WHITE)
    d.ellipse([cx - w * 0.12, top + h * 0.82, cx + w * 0.12, top + h * 0.82 + w * 0.24], fill=WHITE)
    d.ellipse([cx - w * 0.07, top, cx + w * 0.07, top + h * 0.14], fill=WHITE)
    return img.resize((size, size), Image.LANCZOS)


for name, px in DENSITIES.items():
    folder = os.path.join(RES, "mipmap-" + name)
    os.makedirs(folder, exist_ok=True)
    bell(px, 0.62, BLUE).save(os.path.join(folder, "ic_launcher.png"))
    bell(px, 0.58, BLUE, circle=True).save(os.path.join(folder, "ic_launcher_round.png"))
    fg = int(px * 108 / 48)
    bell(fg, 0.40).save(os.path.join(folder, "ic_launcher_foreground.png"))

values = os.path.join(RES, "values")
os.makedirs(values, exist_ok=True)
with open(os.path.join(values, "ic_launcher_background.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n'
            '    <color name="ic_launcher_background">#2345F0</color>\n</resources>\n')
print("icons written")
