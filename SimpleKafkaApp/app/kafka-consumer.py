#!/usr/bin/env python3
import time

from kafka import KafkaConsumer

encoding = 'utf-8'

topic = 'simple-kafka'
consumer = KafkaConsumer(topic, bootstrap_servers=['kafka:9092'])

print(f"'{topic}' consumer is up and running...")
for raw_msg in consumer:
    str_msg = raw_msg.value.decode(encoding)
    print(f"Received message: [{str_msg}]")
    time.sleep(1)
