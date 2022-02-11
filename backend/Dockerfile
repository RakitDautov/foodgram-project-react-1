FROM python:3.8.5

WORKDIR /app/backend
COPY . ./
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]