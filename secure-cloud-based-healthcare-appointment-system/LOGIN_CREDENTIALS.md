# DocBook - Login Credentials

## ⚠️ Default Password
**ALL users use the same default password:** `aaa`

**IMPORTANT:** Change all default passwords before deploying to production!

---

## Admin Account

| Username | Email | Full Name | Password |
|----------|-------|-----------|----------|
| admin | admin@docbook.com | Admin User | aaa |

**Important:** The `admin` user is NOT in `fixtures/initial_data.json`. You must create/upgrade it by running:

```bash
python create_admin.py
```

**Admin URLs (two different panels):**

| Panel | URL |
|-------|-----|
| DocBook admin dashboard (charts, reports) | http://127.0.0.1:8000/admin/ |
| Django built-in admin (database tables) | http://127.0.0.1:8000/super-admin/ |

Admin access requires `is_superuser=True` and `is_staff=True`. If `admin` behaves like a doctor, run `create_admin.py` again to fix the account.

---

## Doctor Accounts (15 total)

| Username | Email | Full Name | Password |
|----------|-------|-----------|----------|
| doctor1 | segun.ogunleye@example.com | Segun Ogunleye | aaa |
| doctor2 | folake.babatunde@example.com | Folake Babatunde | aaa |
| doctor3 | amina.adebayo@example.com | Amina Adebayo | aaa |
| doctor4 | ibrahim.chukwu@example.com | Ibrahim Chukwu | aaa |
| doctor5 | ifeoma.ogunleye@example.com | Ifeoma Ogunleye | aaa |
| doctor6 | funke.ogunleye@example.com | Funke Ogunleye | aaa |
| doctor7 | ibrahim.adebayo@example.com | Ibrahim Adebayo | aaa |
| doctor8 | chioma.adeyemi@example.com | Chioma Adeyemi | aaa |
| doctor9 | aisha.adeleke@example.com | Aisha Adeleke | aaa |
| doctor10 | ngozi.musa@example.com | Ngozi Musa | aaa |
| doctor11 | chioma.adebayo@example.com | Chioma Adebayo | aaa |
| doctor12 | temitope.adeyemi@example.com | Temitope Adeyemi | aaa |
| doctor13 | segun.okafor@example.com | Segun Okafor | aaa |
| doctor14 | zainab.oluwaseun@example.com | Zainab Oluwaseun | aaa |
| doctor15 | femi.chukwu@example.com | Femi Chukwu | aaa |

---

## Patient Accounts (15 total)

| Username | Email | Full Name | Password |
|----------|-------|-----------|----------|
| patient1 | funke.oluwaseun@example.com | Funke Oluwaseun | aaa |
| patient2 | fatima.adeyemi@example.com | Fatima Adeyemi | aaa |
| patient3 | babatunde.okoro@example.com | Babatunde Okoro | aaa |
| patient4 | adeolu.adeyemi@example.com | Adeolu Adeyemi | aaa |
| patient5 | ngozi.okafor@example.com | Ngozi Okafor | aaa |
| patient6 | zainab.adebayo@example.com | Zainab Adebayo | aaa |
| patient7 | adunni.oluwaseun@example.com | Adunni Oluwaseun | aaa |
| patient8 | chukwuemeka.ibrahim@example.com | Chukwuemeka Ibrahim | aaa |
| patient9 | ngozi.okoro@example.com | Ngozi Okoro | aaa |
| patient10 | ifeoma.musa@example.com | Ifeoma Musa | aaa |
| patient11 | ifeoma.okafor@example.com | Ifeoma Okafor | aaa |
| patient12 | olumide.musa@example.com | Olumide Musa | aaa |
| patient13 | ifeoma.nwankwo@example.com | Ifeoma Nwankwo | aaa |
| patient14 | kolawole.okafor@example.com | Kolawole Okafor | aaa |
| patient15 | aisha.okafor@example.com | Aisha Okafor | aaa |

---

## Where Credentials Are Stored

1. **Fixture File:** `fixtures/initial_data.json`
   - Contains all user data including usernames and hashed passwords
   - Passwords are hashed using PBKDF2-SHA256
   - The hash corresponds to password: `aaa`

2. **Generator Script:** `generate_fixtures.py`
   - Line 6: Comment shows default password is `aaa`
   - Line 171 & 224: Password hash for `aaa`

3. **Documentation:** `README.md`
   - Lines 120-121: Lists default credentials

4. **This File:** `LOGIN_CREDENTIALS.md`
   - Complete list of all credentials

---

## How to Extract Credentials

Run this command to see all credentials:
```bash
python get_credentials.py
```

Or check the database directly:
```bash
python manage.py shell
```

Then in the shell:
```python
from accounts.models import User
for user in User.objects.all():
    print(f"{user.username} | {user.email} | {user.get_full_name()} | Role: {user.role}")
```

---

## Security Note

- All passwords in the fixtures are hashed using PBKDF2-SHA256
- The actual password `aaa` is documented in `generate_fixtures.py`
- **CRITICAL:** Change all default passwords immediately in production!
- Never commit `.env` files or real passwords to version control
