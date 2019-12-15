FROM python:3.6.9-alpine3.9

RUN mkdir /opt/app && pip install --no-cache-dir flask requests
COPY app/ /opt/app
WORKDIR /opt/app

ENTRYPOINT python main.py
