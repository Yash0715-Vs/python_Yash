import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db = "employee"
)
cursor = connection.cursor()
cursor.execute("SELECT name FROM employee")
data = cursor.fetchall()
print(data)
connection.close()