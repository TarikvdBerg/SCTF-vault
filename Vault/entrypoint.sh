#!/bin/sh

sleep 5

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn Vault.wsgi:application --bind 0.0.0.0:8000