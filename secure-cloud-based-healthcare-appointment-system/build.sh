#!/usr/bin/env bash
set -o errexit

echo "Python version:"
python --version

echo "Installing PostgreSQL driver..."
pip install "psycopg2-binary==2.9.9"
python -c "import psycopg2; print('psycopg2 OK')"

pip install -r requirements.txt

# Fix postgres:// URLs from Render/Heroku
if [ -n "$DATABASE_URL" ] && [[ "$DATABASE_URL" == postgres://* ]]; then
  export DATABASE_URL="${DATABASE_URL/postgres:\/\//postgresql:\/\/}"
fi

python manage.py migrate --noinput

# Load demo users and sample data (safe to re-run on deploy)
python manage.py loaddata fixtures/initial_data.json || true
python create_admin.py || true
python seed_doctor_schedules.py || true
python seed_specialities.py || true
python seed_demo_bookings.py || true

python manage.py collectstatic --noinput
