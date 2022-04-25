FROM python:3.8
RUN pip install kafka-python==2.0.2
WORKDIR /app
COPY ./kafka-consumer.py /app/kafka-consumer.py
COPY ./kafka-producer.py /app/kafka-producer.py