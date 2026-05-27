# Security Validation Checklist

Use this guide to demonstrate that the **Secure Cloud-Based Healthcare Management System** satisfies all thesis security requirements.

## 1. Encrypted Logins
1. Register or log in as a user.
2. Open `db.sqlite3` with DB Browser for SQLite (read-only).
3. Inspect `accounts_user.password`.  
   - Expected format: `pbkdf2_sha256$260000$...` (hashed, no plain text).
4. Attempt to log in with a wrong password to confirm Django rejects invalid credentials.
5. View the login page source and verify the CSRF token input exists:
   ```html
   <input type="hidden" name="csrfmiddlewaretoken" value="...">
   ```

## 2. Role-Based Access Control
Use the sample accounts from `fixtures/initial_data.json` (`doctor1`, `patient1`, password `password123`).

| Role      | Allowed URLs                              | Blocked URLs                                      |
|-----------|-------------------------------------------|---------------------------------------------------|
| Patient   | `/patients/dashboard/`, `/bookings/...`   | `/doctors/dashboard/`, `/doctors/profile-settings/` |
| Doctor    | `/doctors/dashboard/`, `/patients/..`     | `/patients/dashboard/`                            |
| Admin     | `/super-admin/`, `/admin/`                | Non-admin users should be denied automatically    |

Steps:
1. Log in as `patient1` and visit `/doctors/dashboard/` → expect redirect or “not authorized”.
2. Log in as `doctor1` and visit `/patients/dashboard/` → expect access denied.
3. Log in as your superuser and confirm full access to `/super-admin/` and `/admin/`.

## 3. HTTPS & Cloud Deployment
1. Prepare `.env` for production:
   ```env
   DEBUG=False
   SECRET_KEY=<secure key>
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```
2. Deploy behind a reverse proxy (e.g., Nginx) with a valid TLS certificate (Let’s Encrypt/Cloudflare).
3. After deployment:
   - Visit `https://yourdomain.com` and confirm the padlock icon.
   - In DevTools → Application → Cookies, verify `sessionid` and `csrftoken` have the **Secure** flag.
   - Open the Network tab, confirm all requests use `https://`.
   - Try `http://yourdomain.com` and ensure it automatically redirects to `https://`.

## 4. Additional Operational Checks
- **Account lockout scenarios**: attempt multiple failed logins to ensure no crash (Django handles gracefully).
- **CSRF protection**: use DevTools to delete the CSRF cookie and submit a form → expect HTTP 403.
- **Session expiry**: set `SESSION_COOKIE_AGE` (optional) for demonstration if needed.

Document the results (screenshots or notes) for each step to include in your thesis appendix. This shows examiners that the solution is tested against the stated security objectives.



