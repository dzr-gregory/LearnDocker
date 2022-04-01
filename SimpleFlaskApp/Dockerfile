# Docker configuration file for SimpleFlaskApp
#
# Build: docker build -t learndocker/simpleflaskapp .
# Run: docker run learndocker/simpleflaskapp

FROM python:3.8

MAINTAINER Grigory Balashov <dzr.gregory@gmail.com>

RUN pip install flask==2.1.1 requests==2.27.1

WORKDIR /simpleflaskapp
COPY templates/ /simpleflaskapp/templates
COPY main.py /simpleflaskapp/main.py
RUN chmod a+x /simpleflaskapp/main.py

ENV FLASK_ENV development

ENTRYPOINT ["/simpleflaskapp/main.py"]
