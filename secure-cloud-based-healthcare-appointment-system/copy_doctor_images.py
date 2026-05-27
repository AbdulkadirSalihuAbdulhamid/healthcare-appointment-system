"""
Script to copy doctor images from static/assets/img to media/profiles
Run this after loading fixtures to ensure doctor images are available.
"""
import os
import shutil
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent
STATIC_IMG_DIR = BASE_DIR / "static" / "assets" / "img"
MEDIA_PROFILES_DIR = BASE_DIR / "media" / "profiles"

# Doctor image files to copy
doctor_images = [
    "dr_aisha_adeleke.jpg.jpg",
    "dr_amina_ademeyi.jpg.jpg",
    "dr_babatunde_adeyemi.jpg.jpg",
    "dr_bukola_obi.jpg.jpg",
    "dr_fatima_musa.jpg",
    "dr_femi.jpg",
    "dr_funke_okafor.jpg.png",
    "dr_halima_musa.jpg.jpg",
    "dr_ibrahim_nwankwo.jpg.jpg",
    "dr_ifeoma_adeyemi.jpg.jpg",
    "dr_segun_ibrahim.jpg.jpg",
]

def copy_doctor_images():
    """Copy doctor images from static to media/profiles directory"""
    # Create media/profiles directory if it doesn't exist
    MEDIA_PROFILES_DIR.mkdir(parents=True, exist_ok=True)
    
    copied = 0
    skipped = 0
    
    for img_file in doctor_images:
        src = STATIC_IMG_DIR / img_file
        dst = MEDIA_PROFILES_DIR / img_file
        
        if src.exists():
            try:
                shutil.copy2(src, dst)
                print(f"[OK] Copied: {img_file}")
                copied += 1
            except Exception as e:
                print(f"[ERROR] Error copying {img_file}: {e}")
                skipped += 1
        else:
            print(f"[WARNING] Not found: {img_file}")
            skipped += 1
    
    print(f"\nSummary: {copied} copied, {skipped} skipped/not found")
    print(f"Images are now in: {MEDIA_PROFILES_DIR}")

if __name__ == "__main__":
    copy_doctor_images()





