#!/usr/bin/env python
"""Seed weekly appointment time ranges for every active doctor."""

import os
from datetime import time

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docbook.settings")
django.setup()

from accounts.models import User
from doctors.models.general import (
    Friday,
    Monday,
    Saturday,
    Sunday,
    Thursday,
    TimeRange,
    Tuesday,
    Wednesday,
)

DAY_MODELS = [
    Sunday,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
]

# Two blocks per weekday = many 30-minute bookable slots (08:00–12:00, 13:00–17:00)
WEEKDAY_RANGES = [
    (time(8, 0), time(12, 0)),
    (time(13, 0), time(17, 0)),
]
SATURDAY_RANGES = [(time(9, 0), time(14, 0))]
SUNDAY_RANGES = [(time(10, 0), time(14, 0))]


def _add_ranges(day_obj, ranges):
    day_obj.time_range.clear()
    for start, end in ranges:
        tr, _ = TimeRange.objects.get_or_create(
            start=start, end=end, defaults={"slots_per_hour": 2}
        )
        day_obj.time_range.add(tr)


def seed():
    doctors = User.objects.filter(
        role=User.RoleChoices.DOCTOR, is_active=True, is_superuser=False
    )
    if not doctors.exists():
        print("[ERROR] No doctors found. Run loaddata first.")
        return

    updated = 0
    for doctor in doctors:
        for day_index, day_model in enumerate(DAY_MODELS):
            day_obj, _ = day_model.objects.get_or_create(user=doctor)
            if day_index == 0:
                ranges = SUNDAY_RANGES
            elif day_index == 6:
                ranges = SATURDAY_RANGES
            else:
                ranges = WEEKDAY_RANGES
            _add_ranges(day_obj, ranges)
        updated += 1

    print(f"[OK] Seeded schedules for {updated} doctor(s).")
    print("Each doctor: Mon–Fri 8–12 & 1–5, Sat 9–2, Sun 10–2 (30-min slots).")


if __name__ == "__main__":
    seed()
