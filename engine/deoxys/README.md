Deoxys handles the incoming code type<string> and pass it in the executable format to celery. Celery then schedules and executes the code and sends the order objects to RabbitMQ Queue.

From RabbitMQ, order_manager processes the orders further.
