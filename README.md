# Django Example for Convox

A Django polls application ready to deploy on Convox.

This example demonstrates how to deploy a Django application with PostgreSQL on Convox. The polls app showcases database migrations, static file handling, and the Django admin interface - everything you need to get your Django project started.

Deploy to Convox Cloud for a fully-managed platform experience, or to your own Convox Rack for complete control over your infrastructure. Either way, you'll get automatic SSL, load balancing, and zero-downtime deployments out of the box.

## Deploy to Convox Cloud

1. **Create a Cloud Machine** at [console.convox.com](https://console.convox.com)

2. **Create the app**:
```bash
convox cloud apps create django -i your-machine-name
```

3. **Deploy the app**:
```bash
convox cloud deploy -a django -i your-machine-name
```

4. **Run database migrations**:
```bash
convox cloud run migrate "python manage.py migrate" -a django -i your-machine-name
```

5. **Load sample data**:
```bash
convox cloud run web "python manage.py load_sample_data" -a django -i your-machine-name
```

6. **View your app**:
```bash
convox cloud services -a django -i your-machine-name
```

Visit `<your-url>/polls/` to see the polls app!

## Deploy to Convox Rack

1. **Create the app**:
```bash
convox apps create django
```

2. **Deploy the app**:
```bash
convox deploy -a django
```

3. **Run database migrations**:
```bash
convox run migrate "python manage.py migrate" -a django
```

4. **Load sample data**:
```bash
convox run web "python manage.py load_sample_data" -a django
```

5. **View your app**:
```bash
convox services -a django
```

Visit `<your-url>/polls/` to see the polls app!

## Optional Setup

### Create Admin User

Cloud:
```bash
convox cloud run web "python manage.py createsuperuser" -a django -i your-machine-name
```

Rack:
```bash
convox run web "python manage.py createsuperuser" -a django
```

### Set Production SECRET_KEY

Generate secure key:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Cloud:
```bash
convox cloud env set SECRET_KEY=<generated-key> -a django -i your-machine-name
```

Rack:
```bash
convox env set SECRET_KEY=<generated-key> -a django
```

## Local Development

```bash
pip install -r requirements.txt
export SECRET_KEY='dev-secret-key'
export DATABASE_URL='sqlite:///db.sqlite3'
python manage.py migrate
python manage.py runserver
```

## Project Structure

- Django 4.2 with PostgreSQL
- Example polls application
- WhiteNoise for static files
- Gunicorn WSGI server

## Common Commands

### View logs

Cloud:
```bash
convox cloud logs -a django -s web -i your-machine-name
```

Rack:
```bash
convox logs -a django
```

### Django shell

Cloud:
```bash
convox cloud run web "python manage.py shell" -a django -i your-machine-name
```

Rack:
```bash
convox run web "python manage.py shell" -a django
```

### Export database

Cloud:
```bash
convox cloud resources export database -a django -i your-machine-name --file backup.sql
```

Rack:
```bash
convox resources export database -a django --file backup.sql
```