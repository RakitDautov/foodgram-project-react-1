FROM python:3.8.5

WORKDIR /backend
COPY . ./
RUN pip install -r requirements.txt
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:8000