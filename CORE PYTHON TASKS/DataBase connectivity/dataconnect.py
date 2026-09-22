import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db = "bank"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM student")
data = cursor.fetchall()
print(data)
print("Data fetched successfully")