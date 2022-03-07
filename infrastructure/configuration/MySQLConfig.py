import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'pruebas',
  'password': 'VGbt3Day5R',
  'host': '3.130.126.210',
  'port': '3309',
  'database': 'habi_db'
}


def connect():
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)



