#! /bin/bash

python3 manage.py makemigrations users

python3 manage.py makemigrations foodgram

python3 manage.py migrate --no-input

python3 manage.py collectstatic --no-input

gunicorn backend.wsgi:application --bind 0.0.0.0:8000
