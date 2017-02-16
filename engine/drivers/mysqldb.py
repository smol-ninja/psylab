import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector import errorcode

class DatabaseObject(object):
    def __init__(self):
        DB_NAME = settings.get_database()

        self.connpool = MySQLConnectionPool(user=settings.DatabaseConfig.USERNAME,
                                            password=settings.DatabaseConfig.PASSWORD,
                                            host=settings.DatabaseConfig.HOST,
                                            pool_name="mypool",
                                            pool_size=1,
                                            autocommit=True,
                                            database=DB_NAME
                                            )

        self.cnx_main = self.connpool.get_connection()
        self.cur_main = self.cnx_main.cursor()
