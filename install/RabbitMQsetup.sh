sudo bash
echo "deb http://www.rabbitmq.com/debian/ testing main" >> /etc/apt/sources.list
curl http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | sudo apt-key add -
apt-get update
# install rabbitmq:broker
apt-get install rabbitmq-server
rabbitmq-plugins enable rabbitmq_management
service rabbitmq-server restart
# installing puka
pip install pika

# if guest credentials not working
# creating a test user with test password
rabbitmqctl add_user test test
rabbitmqctl set_user_tags test administrator
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
