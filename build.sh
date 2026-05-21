#!/usr/bin/env bash
# Exit on error
set -o errexit

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations (This automatically triggers the code above!)
python manage.py migrate

# Start both web and worker using Honcho
honcho start
