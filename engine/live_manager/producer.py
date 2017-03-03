import pika
import time
import json
HEARTBEAT_INTERVAL=2
conn_params = pika.ConnectionParameters(
        heartbeat_interval=HEARTBEAT_INTERVAL
    )
connection = pika.BlockingConnection()
channel = connection.channel()
channel.queue_declare(queue='hello') # Declare a queue
"""
Encoding JSON
"""
body=json.dumps(
                {
                  "sid":1234,
                  "side":"buy",
                  "quantity":12,
                  "orderType":"market",
                  "price":23
                }
                )
while True:
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=body)
    print "SENT"
    time.sleep(1)
connection.close()
