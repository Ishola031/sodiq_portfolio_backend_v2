web: gunicorn sodiq_portfolio.wsgi:application --bind 0.0.0.0:$PORT
worker: celery -A sodiq_portfolio worker --loglevel=info --concurrency=1