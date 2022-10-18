#!/bin/sh


python manage.py migrate --run-syncdb


gunicorn SportNews.wsgi:application --bind 0.0.0.0:8000 --reload  -w 4
