#!/bin/sh


python manage.py migrate --run-syncdb
#python manage.py collectstatic --no-input

gunicorn SportNews.wsgi:application --bind 0.0.0.0:8000 --reload  -w 4
