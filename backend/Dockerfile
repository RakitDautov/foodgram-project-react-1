FROM python:3.9

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
RUN chmod +x entrypoint.sh

#CMD gunicorn backend.wsgi:application --bind 0.0.0.0:8000

ENTRYPOINT ["/app/entrypoint.sh"]