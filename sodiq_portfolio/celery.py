from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sodiq_portfolio.settings")

app = Celery("sodiq_portfolio")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
