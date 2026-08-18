#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser safely
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='sodiqadmin').exists():
    User.objects.create_superuser('sodiqadmin', 'sannisodiq031@gmail.com', 'Ishola@031');
    print('✔ Superuser created');
else:
    print('⚠️ Superuser already exists');
"