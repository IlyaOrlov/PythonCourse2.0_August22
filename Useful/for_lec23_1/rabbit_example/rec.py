import pika
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello3', durable=True)


def callback(ch, method, properties, body):
    print(f'Start processing {body.decode()}')
    t = time.time()
    time.sleep(random.randint(1, 5))
    print(f'Processed for {time.time() - t:.2f} sec.')


channel.basic_consume(queue='hello3', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
