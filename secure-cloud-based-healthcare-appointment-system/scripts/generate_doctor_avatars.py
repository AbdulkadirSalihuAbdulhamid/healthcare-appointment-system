#!/usr/bin/env python
"""Generate bundled doctor portrait images (doctor1.jpg … doctor15.jpg)."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "static" / "assets" / "img" / "doctors"

PALETTES = [
    ("#1565C0", "#42A5F5"),
    ("#2E7D32", "#66BB6A"),
    ("#6A1B9A", "#AB47BC"),
    ("#C62828", "#EF5350"),
    ("#EF6C00", "#FFA726"),
    ("#00838F", "#26C6DA"),
    ("#4527A0", "#7E57C2"),
    ("#AD1457", "#EC407A"),
    ("#283593", "#5C6BC0"),
    ("#33691E", "#9CCC65"),
    ("#4E342E", "#8D6E63"),
    ("#37474F", "#78909C"),
    ("#00695C", "#26A69A"),
    ("#827717", "#D4E157"),
    ("#1B5E20", "#81C784"),
]


def draw_avatar(path: Path, initials: str, colors: tuple[str, str]) -> None:
    size = 400
    img = Image.new("RGB", (size, size), colors[0])
    draw = ImageDraw.Draw(img)
    draw.ellipse((20, 20, size - 20, size - 20), fill=colors[1])
    draw.ellipse((120, 90, 280, 250), fill="#FFE0BD")
    draw.ellipse((155, 175, 195, 205), fill="#5D4037")
    draw.ellipse((205, 175, 245, 205), fill="#5D4037")
    draw.arc((150, 200, 250, 280), 20, 160, fill="#8D6E63", width=4)
    try:
        font = ImageFont.truetype("arial.ttf", 72)
    except OSError:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), initials, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(
        ((size - tw) / 2, size - th - 36),
        initials,
        fill="white",
        font=font,
        stroke_width=2,
        stroke_fill=colors[0],
    )
    img.save(path, "JPEG", quality=88)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i in range(1, 16):
        username = f"doctor{i}"
        initials = f"D{i}"
        colors = PALETTES[(i - 1) % len(PALETTES)]
        out = OUT_DIR / f"{username}.jpg"
        draw_avatar(out, initials, colors)
        print(f"Wrote {out}")
    print(f"[OK] {len(list(OUT_DIR.glob('doctor*.jpg')))} doctor avatars in {OUT_DIR}")


if __name__ == "__main__":
    main()
