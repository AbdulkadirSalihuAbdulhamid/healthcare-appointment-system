#!/usr/bin/env python
"""Create Speciality records from doctor profile data."""

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "docbook.settings")
django.setup()

from accounts.models import User
from core.models import Speciality


def seed():
    names = (
        User.objects.filter(role=User.RoleChoices.DOCTOR)
        .exclude(profile__specialization__isnull=True)
        .exclude(profile__specialization="")
        .values_list("profile__specialization", flat=True)
        .distinct()
    )
    created = 0
    for name in names:
        _, was_created = Speciality.objects.get_or_create(
            name=name,
            defaults={
                "description": f"Medical services in {name}.",
                "is_active": True,
            },
        )
        if was_created:
            created += 1
    print(f"[OK] Specialities in database: {Speciality.objects.count()} ({created} new).")


if __name__ == "__main__":
    seed()
