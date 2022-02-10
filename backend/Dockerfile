FROM python:3.8.5

WORKDIR /app
COPY requirements.txt ./app/backend
RUN pip install -r requirements.txt
COPY . ./
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:8000