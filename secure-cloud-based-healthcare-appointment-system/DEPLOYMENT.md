# DocBook - Cloud Deployment Guide

This guide provides instructions for deploying DocBook to a cloud server.

## Prerequisites

- A cloud server (AWS EC2, DigitalOcean, Heroku, Railway, etc.)
- Domain name (optional but recommended)
- SSL certificate (for HTTPS)
- Python 3.8+ installed on the server

## Quick Deployment Steps

### 1. Server Setup

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip python3-venv -y

# Install PostgreSQL (recommended) or use SQLite for small deployments
sudo apt install postgresql postgresql-contrib -y

# Install Nginx (for serving static files and reverse proxy)
sudo apt install nginx -y
```

### 2. Clone and Setup Project

```bash
# Clone your repository
git clone <your-repo-url>
cd secure-cloud-based-healthcare-appointment-system/secure-cloud-based-healthcare-appointment-system

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn  # Production WSGI server
```

### 3. Environment Configuration

Create a `.env` file:

```env
SECRET_KEY=your-very-secure-secret-key-here-generate-with-django
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,your-server-ip
DATABASE_URL=postgresql://user:password@localhost/dbname  # If using PostgreSQL
```

Generate a secure SECRET_KEY:
```bash
python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Database Setup

```bash
# Run migrations
python manage.py migrate

# Load initial data (optional)
python generate_fixtures.py
python manage.py loaddata fixtures/initial_data.json
python copy_doctor_images.py  # Copy doctor images to media folder

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

### 5. Configure Gunicorn

Create `gunicorn_config.py`:

```python
bind = "127.0.0.1:8000"
workers = 3
worker_class = "sync"
timeout = 120
keepalive = 5
```

### 6. Create Systemd Service

Create `/etc/systemd/system/docbook.service`:

```ini
[Unit]
Description=DocBook Gunicorn daemon
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/secure-cloud-based-healthcare-appointment-system/secure-cloud-based-healthcare-appointment-system
ExecStart=/path/to/venv/bin/gunicorn \
    --config gunicorn_config.py \
    docbook.wsgi:application

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable docbook
sudo systemctl start docbook
sudo systemctl status docbook
```

### 7. Configure Nginx

Create `/etc/nginx/sites-available/docbook`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Redirect HTTP to HTTPS (after SSL setup)
    # return 301 https://$server_name$request_uri;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/secure-cloud-based-healthcare-appointment-system/secure-cloud-based-healthcare-appointment-system/staticfiles/;
    }

    location /media/ {
        alias /path/to/secure-cloud-based-healthcare-appointment-system/secure-cloud-based-healthcare-appointment-system/media/;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/docbook /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 8. SSL Certificate (Let's Encrypt)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal is set up automatically
```

### 9. Firewall Configuration

```bash
# Allow HTTP, HTTPS, and SSH
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

## Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY` in `.env`
- [ ] `.env` file not in version control (already in `.gitignore`)
- [ ] HTTPS enabled with SSL certificate
- [ ] All default passwords changed
- [ ] Database credentials secured
- [ ] Regular backups configured
- [ ] Firewall rules configured
- [ ] Security headers enabled (HSTS, etc.)

## Alternative: Platform-as-a-Service (PaaS)

### Heroku

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: gunicorn docbook.wsgi:application --bind 0.0.0.0:$PORT
   ```
3. Deploy:
   ```bash
   heroku create your-app-name
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   git push heroku main
   ```

### Railway / Render

Similar process - connect GitHub repo and configure environment variables.

## Monitoring and Maintenance

- Monitor logs: `sudo journalctl -u docbook -f`
- Check Nginx logs: `sudo tail -f /var/log/nginx/error.log`
- Regular updates: `pip install --upgrade -r requirements.txt`
- Database backups: Set up automated backups

## Troubleshooting

- **502 Bad Gateway**: Check if Gunicorn is running (`sudo systemctl status docbook`)
- **Static files not loading**: Run `python manage.py collectstatic`
- **Permission errors**: Check file ownership (`sudo chown -R www-data:www-data /path/to/project`)

## Support

For issues, check:
- Django logs: `sudo journalctl -u docbook`
- Nginx logs: `/var/log/nginx/`
- Application logs in your project directory





