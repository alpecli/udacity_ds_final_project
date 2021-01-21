from kafka import KafkaConsumer
import time
import json

def consume_messages(kafka_consumer):
    for message in kafka_consumer:
        print(message.value)
        time.sleep(1)

def generate_consumer():
    kafka_consumer = KafkaConsumer(
        bootstrap_servers='localhost:9092',
        #auto_offset_reset='earliest',
        value_deserializer=lambda b_msg: json.loads(b_msg.decode('utf-8')),
    )
    kafka_consumer.subscribe('crimes')
    return kafka_consumer

if __name__ == '__main__':
    consumer = generate_consumer()
    consume_messages(consumer)