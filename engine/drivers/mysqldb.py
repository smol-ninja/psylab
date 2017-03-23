import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import errorcode

from engine.order_manager import settings

class SQLManager(object):
    def __init__(self):
        self.connect_to_database()

    def connect_to_database(self):
        DB_NAME = settings.get_database()

        self.connpool = MySQLConnectionPool(user=settings.DatabaseConfig.USERNAME,
                                            password=settings.DatabaseConfig.PASSWORD,
                                            host=settings.DatabaseConfig.HOST,
                                            pool_name="order_manager",
                                            pool_size=5,
                                            autocommit=True,
                                            database=DB_NAME
                                            )
        self.cnx1 = self.connpool.get_connection()
        self.cur1 = self.cnx1.cursor()
        self.cnx2 = self.connpool.get_connection()
        self.cur2 = self.cnx2.cursor()
        self.cnx3 = self.connpool.get_connection()
        self.cur3 = self.cnx3.cursor()
        self.cnx4 = self.connpool.get_connection()
        self.cur4 = self.cnx4.cursor()
        self.cnx5 = self.connpool.get_connection()
        self.cur5 = self.cnx5.cursor()
