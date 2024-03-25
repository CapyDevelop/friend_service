FROM python:3.11-slim

RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
#COPY .env_docker .env
COPY alembic_docker.ini alembic.ini

CMD ["sh", "start.sh"]