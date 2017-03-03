import puka

# declare and connect a consumer
consumer = puka.Client("amqp://localhost/")
connect_promise = consumer.connect()
consumer.wait(connect_promise)

# bind the queue to newsletter exchange
consumer.queue_declare(queue='hello')
bind_promise = consumer.queue_bind(exchange='newsletter', queue='hello')
consumer.wait(bind_promise)

# start waiting for messages on the queue created beforehand and print them out
message_promise = consumer.basic_consume(queue='hello', no_ack=True)

while True:
    message = consumer.wait(message_promise)
    print "GOT: %r" % message['body']

consumer.close()
