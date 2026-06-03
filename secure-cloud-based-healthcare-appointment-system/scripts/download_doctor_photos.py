#!/usr/bin/env python
"""
Download 15 professional portrait photos for doctor1 … doctor15.
Source: randomuser.me (free to use for demos / mockups).
Run once locally, commit the JPGs, then deploy — do not re-run on Render.
"""

import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "static" / "assets" / "img" / "doctors"
API = (
    "https://randomuser.me/api/?results=15&inc=picture"
    "&nat=us,gb,ca,au,ie,fr,de,es,it,nl"
)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(API, timeout=60) as resp:
        data = json.load(resp)

    for i, person in enumerate(data["results"], start=1):
        url = person["picture"]["large"]
        dest = OUT_DIR / f"doctor{i}.jpg"
        urllib.request.urlretrieve(url, dest)
        print(f"Saved {dest.name} ({url})")

    print(f"[OK] 15 photos in {OUT_DIR}")


if __name__ == "__main__":
    main()
