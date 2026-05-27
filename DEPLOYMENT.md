# Cloud Deployment Guide (Render Example)

This guide shows how to deploy **Secure Cloud-Based Healthcare Management System** on [Render](https://render.com/) using Gunicorn. The same steps apply to Railway, Fly.io, or any Ubuntu VPS.

## 1. Prepare the Project
1. Ensure all code is committed and pushed to GitHub.
2. Create a `.env.prod` file (not committed) with production settings:
   ```env
   DEBUG=False
   SECRET_KEY=<generate-a-strong-value>
   ALLOWED_HOSTS=your-domain.com,www.your-domain.com
   DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DB  # provided by Render
   ```
3. Update `requirements.txt` (already includes `gunicorn`).

## 2. Create a Render Web Service
1. Sign up / log in to [Render](https://render.com/).
2. Click **New +** → **Web Service**.
3. Connect your GitHub repo and choose the project.
4. Set:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn docbook.wsgi:application --bind 0.0.0.0:$PORT`
5. Add environment variables in the Render dashboard:
   - `DJANGO_SETTINGS_MODULE=docbook.settings`
   - Copy values from `.env.prod` (SECRET_KEY, ALLOWED_HOSTS, DATABASE_URL, etc.).

## 3. Database
1. In Render, create a **PostgreSQL** instance.
2. Copy the connection string and set it as `DATABASE_URL`.
3. Deploy the web service. Once it’s live, open the Render shell:
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py createsuperuser
   ```

## 4. HTTPS & Domain
1. Render automatically provisions HTTPS for the default `onrender.com` domain.
2. To use a custom domain:
   - Add the domain in Render → connect CNAME to Render’s hostname.
   - Wait for SSL certificate provisioning (Let’s Encrypt).
3. In `.env.prod`, set `ALLOWED_HOSTS` to include both the Render domain and your custom domain.

## 5. Background Jobs (Optional)
If you need scheduled tasks (daily reports etc.), create a Render Cron Job that runs:
```bash
python manage.py <management_command>
```

## 6. Health Checks
After deployment:
- Visit `https://<your-app>.onrender.com` (or your custom domain).
- Run the `docs/SECURITY_VALIDATION.md` checklist against the live site to document HTTPS enforcement, RBAC, and encrypted logins.

You now have a secure, cloud-hosted instance that satisfies the thesis requirement for easy accessibility and HTTPS protection.



