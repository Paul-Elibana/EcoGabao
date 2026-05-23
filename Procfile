web: python manage.py migrate --no-input && python manage.py createsuperuser --no-input 2>/dev/null; gunicorn config.wsgi:application
