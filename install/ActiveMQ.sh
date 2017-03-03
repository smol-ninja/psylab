wget http://apache.mirror.pop-sc.rnp.br/apache/activemq/apache-activemq/5.6.0/apache-activemq-5.6.0-bin.tar.gz
tar zxvf apache-activemq-5.6.0-bin.tar.gz
#Opcional: Change activemq for a place more appropriate
   sudo mv apache-activemq-5.6.0 /usr/local/activemq
cd [activemq_install_dir]/bin
chmod 755 activemq

#Automatic Starting
sudo vi /etc/init.d/activemq

- Cole o código abaixo no arquivo criado acima
# activemq auto-start
#
# description: Auto-starts tomcat
# processname: activemq
# pidfile: /var/run/activemq.pid

export JAVA_HOME=/usr/lib/jvm/java-6-sun

case $1 in
start)
        sh /usr/local/activemq/bin/activemq start
        ;;
stop)
        sh /usr/local/activemq/bin/activemq stop
        ;;
restart)
        sh /usr/local/activemq/bin/activemq stop
        sh /usr/local/activemq/bin/activemq start
        ;;
esac
exit 0

- Tornando-o executável
sudo chmod 755 /etc/init.d/activemq

- Criando links para inicialização automática sudo ln -s /etc/init.d/activemq /etc/rc1.d/K98activemq
sudo ln -s /etc/init.d/activemq /etc/rc2.d/S98activemq
