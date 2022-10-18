#!/bin/sh


python manage.py migrate --run-syncdb


gunicorn web.wsgi:application --bind 0.0.0.0:8000 --reload  -w 4
