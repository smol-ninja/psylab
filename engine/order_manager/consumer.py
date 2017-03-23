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

def obj_consumer():
    """
    Usage:Get objects from rabbitMQ queue
    """
    HEARTBEAT_INTERVAL=2
    conn_params = pika.ConnectionParameters(
            heartbeat_interval=HEARTBEAT_INTERVAL
        )
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()
    for method_frame, properties, body in channel.consume('hello'):
        json_to_object(body)
        channel.basic_ack(method_frame.delivery_tag)
    # Cancel the consumer and return any pending objects
    requeued_messages = channel.cancel()
    print('Requeued %i messages' % requeued_messages)
    connection.close()

def json_to_object(body):
    """
    Usage:Decoding json to object
    """
    js=json.loads(body)
    orderObj=OrderObject(js["sid"],js["side"],js["quantity"],js["orderType"],js["price"])
    if orderObj.get_value():
        print 'write date'
    else:
        print 'retry'
obj_consumer()
