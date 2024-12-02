FROM python:3.12-alpine3.20

COPY requirements.txt /temp/requirements.txt
COPY service /service
WORKDIR /service
EXPOSE 8000

RUN apk add --no-cache postgresql-client build-base postgresql-dev libffi-dev

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

CMD ["celery", "-A", "sssgoul", "worker", "--loglevel=info"]

USER service-user