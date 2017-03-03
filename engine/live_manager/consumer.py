import pika
HEARTBEAT_INTERVAL=2
conn_params = pika.ConnectionParameters(
        heartbeat_interval=HEARTBEAT_INTERVAL,
        connection_attempts=10000,
        retry_delay=10
    )
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()
for method_frame, properties, body in channel.consume('hello'):

    # Display the message parts and ack the message
    # print(method_frame, properties, body)
    print body
    channel.basic_ack(method_frame.delivery_tag)

# Cancel the consumer and return any pending messages
requeued_messages = channel.cancel()
print('Requeued %i messages' % requeued_messages)
connection.close()
