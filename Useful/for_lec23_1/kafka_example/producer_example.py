import kafka


if __name__ == "__main__":
    producer = kafka.KafkaProducer(bootstrap_servers=["127.0.0.1:9092"])
    producer.send("example_topic", 'example_message_1'.encode())
    producer.send("example_topic", 'example_message_2'.encode())
    # Для немедленной отправки без буферизации
    producer.flush()
