#!/usr/bin/env python
"""Create sample appointments so admin reports have data to display."""

import os
import random
from datetime import timedelta

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docbook.settings")
django.setup()

from django.utils import timezone

from accounts.models import User
from bookings.models import Booking


def seed():
    doctors = list(User.objects.filter(role=User.RoleChoices.DOCTOR)[:5])
    patients = list(User.objects.filter(role=User.RoleChoices.PATIENT)[:5])
    if not doctors or not patients:
        print("[ERROR] Need at least one doctor and one patient in the database.")
        print("Run: python manage.py loaddata fixtures/initial_data.json")
        return

    statuses = ["pending", "confirmed", "completed", "cancelled"]
    today = timezone.now().date()
    created = 0

    times = ["09:00:00", "10:30:00", "14:00:00", "16:00:00"]
    for day_offset in range(0, 30, 3):
        appt_date = today - timedelta(days=day_offset)
        for slot, appt_time in enumerate(times[:2]):
            doctor = doctors[slot % len(doctors)]
            patient = random.choice(patients)
            status = random.choice(statuses)
            Booking.objects.get_or_create(
                doctor=doctor,
                appointment_date=appt_date,
                appointment_time=appt_time,
                defaults={
                    "patient": patient,
                    "status": status,
                },
            )
            created += 1

    print(f"[OK] Created {created} sample appointments.")
    print("Refresh: http://127.0.0.1:8000/admin/reports/appointments/")


if __name__ == "__main__":
    seed()
