FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]