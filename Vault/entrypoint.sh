#!/bin/sh

sleep 5

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py cron add
gunicorn Vault.wsgi:application --bind 0.0.0.0:8000