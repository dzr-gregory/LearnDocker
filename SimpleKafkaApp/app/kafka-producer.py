#!/usr/bin/env python3
import random
import time

from kafka import KafkaProducer

encoding = 'utf-8'

topic = 'simple-kafka'
producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

print(f"'{topic}' producer is up and running...")

idx = 1
while True:
    msg = f"Random message {idx} from kafka producer"
    producer.send(topic, msg.encode(encoding))
    time.sleep(random.randint(1, 3))
    print(f"Message [{msg}] was sent")
    idx += 1
