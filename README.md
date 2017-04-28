Psylab Version 1.0

Psylab is a python based trading simulator. The idea is to build an ecosystem where talents can research and develop trading algorithms in the most efficient environment and the least number of lines.

Please note that any unauthorized copying of the source code and any associated documentation files (the "Software"), via any medium is strictly prohibited. Before contributing to psylab, you must sign Individual CLA License attached with this project.

All portions of this software are Copyright (c) 2017 Imba Enterprises Pvt. Ltd. All Rights Reserved.

Happy coding!

************************ virtualenv *******************************
Create a folder env/ in the project directory and then run
virtualenv .
inside env/

Activate virtualenv: source env/bin/activate
Deactivate: deactivate

************************* Setup Psylab *****************************
python install/setup.py

********************* Setting up Mongo DB **************************
Follow the instruction at https://docs.mongodb.com/master/tutorial/install-mongodb-on-ubuntu/

************************* Setup RabbitMQ *****************************
sudo apt-get install rabbitmq-server

To enale rabbitmq UI run the following:

rabbitmq-plugins enable rabbitmq_management

if guest credentials not working
creating a test user with test password

rabbitmqctl add_user test test
rabbitmqctl set_user_tags test administrator
rabbitmqctl set_permissions -p / test ".*" ".*" ".*"

********************* Adding psylab to sys.pth ********************
Create a .pth file in lib/python2.7/site-packages and add /path/to/psylab/ to it

********************* Installing TA-Lib ***************************
$ untar ta-lib-0.4.0-src.tar.gz ans cd
$ ./configure --prefix=/usr
$ make
$ sudo make install
$ (env) pip install TA-Lib
