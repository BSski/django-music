#!/usr/bin/env bash
python manage.py collectstatic --no-input

(cd api; gunicorn api.wsgi:application --bind 0.0.0.0:$PORT --workers 3)