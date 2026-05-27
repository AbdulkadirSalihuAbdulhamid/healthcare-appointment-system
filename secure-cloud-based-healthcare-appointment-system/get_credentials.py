#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to extract all login credentials from fixtures"""

import json

# Load fixtures
with open('fixtures/initial_data.json', 'r', encoding='utf-8') as f:
    fixtures = json.load(f)

# Extract users
users = [item for item in fixtures if item['model'] == 'accounts.user']

print("=" * 80)
print("DOCBOOK - ALL LOGIN CREDENTIALS")
print("=" * 80)
print("\n[IMPORTANT] DEFAULT PASSWORD FOR ALL USERS: password123")
print("=" * 80)

# Doctors
print("\nDOCTOR ACCOUNTS:")
print("-" * 80)
print(f"{'Username':<15} | {'Email':<35} | {'Full Name':<30}")
print("-" * 80)
for user in users:
    if user['fields']['role'] == 'doctor':
        username = user['fields']['username']
        email = user['fields'].get('email', 'N/A')
        first_name = user['fields'].get('first_name', '')
        last_name = user['fields'].get('last_name', '')
        full_name = f"{first_name} {last_name}".strip() or 'N/A'
        print(f"{username:<15} | {email:<35} | {full_name:<30}")

# Patients
print("\nPATIENT ACCOUNTS:")
print("-" * 80)
print(f"{'Username':<15} | {'Email':<35} | {'Full Name':<30}")
print("-" * 80)
for user in users:
    if user['fields']['role'] == 'patient':
        username = user['fields']['username']
        email = user['fields'].get('email', 'N/A')
        first_name = user['fields'].get('first_name', '')
        last_name = user['fields'].get('last_name', '')
        full_name = f"{first_name} {last_name}".strip() or 'N/A'
        print(f"{username:<15} | {email:<35} | {full_name:<30}")

print("\n" + "=" * 80)
print("Total Doctors:", len([u for u in users if u['fields']['role'] == 'doctor']))
print("Total Patients:", len([u for u in users if u['fields']['role'] == 'patient']))
print("=" * 80)

