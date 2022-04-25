#!/usr/bin/env python3

from kafka import KafkaConsumer

encoding = 'utf-8'

topic = 'simple-kafka'
consumer = KafkaConsumer(topic, bootstrap_servers=['kafka:9092'])

for raw_msg in consumer:
    str_msg = raw_msg.value.decode(encoding)
    print(f"Received message: [{str_msg}]")
