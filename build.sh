# #!/usr/bin/env bash
# # Exit on error
# set -o errexit

# # Collect static files
# python manage.py collectstatic --noinput

# # Run database migrations (This automatically triggers the code above!)
# python manage.py migrate

# # Start both web and worker using Honcho
# honcho start


#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate

# Create superuser automatically if it doesn't exist
python manage.py setup_admin