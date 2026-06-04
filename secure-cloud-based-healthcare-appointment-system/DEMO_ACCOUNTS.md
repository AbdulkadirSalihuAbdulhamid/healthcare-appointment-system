# Demonstration accounts

## Live application

| | |
|---|---|
| **URL** | https://healthcare-appointment-system-9a2r.onrender.com |
| **Login** | https://healthcare-appointment-system-9a2r.onrender.com/accounts/login/ |
| **Password** | `aaa` (all demo users) |

## Local application

| | |
|---|---|
| **URL** | http://127.0.0.1:8000/ |
| **Login** | http://127.0.0.1:8000/accounts/login/ |
| **Password** | `aaa` |

---

## Administrator

| Username | Password | Dashboard (live) |
|----------|----------|------------------|
| admin | aaa | https://healthcare-appointment-system-9a2r.onrender.com/admin/ |

Django database admin: https://healthcare-appointment-system-9a2r.onrender.com/super-admin/

Create or reset the admin user locally:

```bash
python create_admin.py
```

## Doctors

| Usernames | Password |
|-----------|----------|
| doctor1, doctor2, … doctor15 | aaa |

Example doctor profile: https://healthcare-appointment-system-9a2r.onrender.com/doctors/doctor1/profile/

## Patients

| Usernames | Password |
|-----------|----------|
| patient1, patient2, … patient15 | aaa |

Example: log in as `patient1`, open **Doctors**, then **Book appointment**.

---

User details (names, emails) are in `fixtures/initial_data.json`.
