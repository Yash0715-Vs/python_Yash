import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db = "employee"
)
cursor = connection.cursor()
query = """INSERT INTO employee (id, name, age, department, salary) VALUES (%s, %s, %s, %s, %s)"""
cursor.execute(query, (1, "John Doe", 30, "IT", 50000))
connection.commit()
data = cursor.fetchall()
print(data)
connection.close()