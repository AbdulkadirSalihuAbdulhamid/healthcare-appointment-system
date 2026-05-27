#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to create a default admin account"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'docbook.settings')
django.setup()

from accounts.models import User
from django.contrib.auth.hashers import make_password

def create_admin():
    """Create a default admin account if it doesn't exist"""
    username = "admin"
    email = "admin@docbook.com"
    password = "aaa"  # Same default password as other users
    
    # Check if admin already exists
    if User.objects.filter(username=username).exists():
        print(f"[INFO] User '{username}' already exists — upgrading to superuser.")
        admin = User.objects.get(username=username)
    else:
        admin = User(
            username=username,
            email=email,
            first_name="Admin",
            last_name="User",
            role=User.RoleChoices.PATIENT,
        )
        print(f"[SUCCESS] Admin account created!")

    admin.is_staff = True
    admin.is_superuser = True
    admin.is_active = True
    admin.set_password(password)
    admin.save()

    print(f"[OK] Username: {username}")
    print(f"[OK] Password: {password}")
    print(f"[OK] is_superuser: {admin.is_superuser}")
    print(f"[OK] is_staff: {admin.is_staff}")

    print("\n" + "=" * 60)
    print("ADMIN LOGIN CREDENTIALS")
    print("=" * 60)
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Admin dashboard: http://127.0.0.1:8000/admin/")
    print(f"Django admin:    http://127.0.0.1:8000/super-admin/")
    print("=" * 60)
    print("\n[IMPORTANT] Change this password in production!")

if __name__ == "__main__":
    create_admin()

