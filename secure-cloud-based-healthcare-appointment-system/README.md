# DocBook — Secure Cloud-Based Healthcare Appointment System

**Author:** Abdulhamid Abdulkadir Salihu  
**Institution:** University of Pécs

Web application for scheduling and managing healthcare appointments. Supports **patients**, **doctors**, and **administrators** with role-based access, secure login, and cloud deployment.

## Online demo (URL and login)

| | |
|---|---|
| **Application URL** | https://healthcare-appointment-system-9a2r.onrender.com |
| **Login page** | https://healthcare-appointment-system-9a2r.onrender.com/accounts/login/ |

**Password for all demo accounts:** `aaa`

| Role | Username | After login |
|------|----------|-------------|
| Administrator | `admin` | https://healthcare-appointment-system-9a2r.onrender.com/admin/ |
| Doctor (example) | `doctor1` | Doctor dashboard / schedule |
| Patient (example) | `patient1` | Patient dashboard / book appointment |

More accounts: `doctor2`–`doctor15`, `patient2`–`patient15` (same password). See `DEMO_ACCOUNTS.md`.

**Suggested test flow:** Log in as `patient1` → Doctors → Book appointment → Log in as `doctor1` → Appointments.

## Features

- Patient registration, doctor search, appointment booking and cancellation
- Doctor schedules, appointment management, prescriptions
- Admin dashboard, reports, and user management
- HTTPS-ready production settings (Render / PostgreSQL / Gunicorn / WhiteNoise)

## Project structure

```
docbook/              # Django settings and URLs
accounts/             # Users, profiles, authentication
doctors/              # Doctor profiles, schedules, appointments
patients/             # Patient dashboard and profile
bookings/             # Appointment booking
core/                 # Home page, reviews, specialities
templates/            # HTML templates
static/               # CSS, JavaScript, images
fixtures/             # Initial demo data
manage.py
requirements.txt
```

## Requirements

- Python 3.10+
- pip

## Local setup

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate   # Linux/macOS

pip install -r requirements.txt

# Optional: create .env with SECRET_KEY, DEBUG=True
python manage.py migrate
python manage.py loaddata fixtures/initial_data.json
python create_admin.py
python seed_doctor_schedules.py
python manage.py collectstatic --noinput
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Demo accounts

See `DEMO_ACCOUNTS.md` for usernames and passwords used in the demonstration dataset.

## Production deployment

See `DEPLOYMENT.md` for cloud deployment steps.

## Licence

Submitted as diploma project work. Third-party libraries are used under their respective licences (see `requirements.txt`).
