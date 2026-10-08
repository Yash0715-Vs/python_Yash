import pymysql

def get_connection():
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="ecommerce"
    )

    return connection

 