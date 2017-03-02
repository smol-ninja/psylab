import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import errorcode

from engine.live_manager import settings

class SQLManager(object):
    def __init__(self):
        self.connect_to_database()

    def connect_to_database(self):
        DB_NAME = settings.get_database()

        self.connpool = MySQLConnectionPool(user=settings.DatabaseConfig.USERNAME,
                                            password=settings.DatabaseConfig.PASSWORD,
                                            host=settings.DatabaseConfig.HOST,
                                            pool_name="mypool",
                                            pool_size=11,
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
        self.cnx6 = self.connpool.get_connection()
        self.cur6 = self.cnx6.cursor()
        self.cnx7 = self.connpool.get_connection()
        self.cur7 = self.cnx7.cursor()
        self.cnx8 = self.connpool.get_connection()
        self.cur8 = self.cnx8.cursor()
        self.cnx9 = self.connpool.get_connection()
        self.cur9 = self.cnx8.cursor()

        self.cnx_mo = self.connpool.get_connection()
        self.cur_mo = self.cnx_mo.cursor()
        self.cnx_main = self.connpool.get_connection()
        self.cur_main = self.cnx_main.cursor()
