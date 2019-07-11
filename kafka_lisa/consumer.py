from kafka import KafkaConsumer
KAFAKA_TOPIC = "netmusic"
if __name__ == "__main__":
    consumer = KafkaConsumer(bootstrap_servers='192.168.31.131:9092')
    consumer.subscribe(KAFAKA_TOPIC)
    for msg in consumer:
        print(msg.value)
    consumer.close()