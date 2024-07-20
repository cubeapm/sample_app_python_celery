FROM ubuntu:22.04

RUN apt-get update && apt-get install -y gcc libffi-dev python3-pip

WORKDIR /flask

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .

RUN pip install -r requirements.txt

RUN opentelemetry-bootstrap -a install

EXPOSE 8000

CMD ["celery", "-A", "celeryapp.celery_app", "worker", "--loglevel=info"]