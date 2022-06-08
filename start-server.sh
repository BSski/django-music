#!/usr/bin/env bash
(cd website; python manage.py collectstatic --no-input)


(cd website; gunicorn website.wsgi:application --bind 0.0.0.0:$PORT --workers 3)