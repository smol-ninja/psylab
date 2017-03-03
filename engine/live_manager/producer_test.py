import puka
import datetime
import time
import json

# declare and connect a producer
producer = puka.Client("amqp://localhost/")
connect_promise = producer.connect()
producer.wait(connect_promise)

# create a fanout exchange
exchange_promise = producer.exchange_declare(exchange='newsletter', type='fanout')
producer.wait(exchange_promise)
producer.queue_declare(queue='hello')
while True:
    message = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}],separators=(',',':'))

    message_promise = producer.basic_publish(exchange='newsletter', routing_key='hello', body=message)
    producer.wait(message_promise)

    print "SENT: %s" % message
    time.sleep(1)
producer.close()
