#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

# Collect static files for Admin panel/DRF browsable API
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate

# Create your admin superuser automatically
python manage.py setup_admin

# Boot up Gunicorn and Celery together via Honcho
honcho start