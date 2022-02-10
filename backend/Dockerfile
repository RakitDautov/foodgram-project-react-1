FROM python:3.8.5

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh
COPY . ./
ENTRYPOINT ["/app/entrypoint.sh"]