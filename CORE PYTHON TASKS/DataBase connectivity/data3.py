import pymysql

connection = pymysql.connect(  # CONNECTION TO DATABASE
    host='localhost',
    user='root',
    password='root',
    db = "employee"
)
cursor = connection.cursor()
query = """INSERT INTO employee (id, name, age, department, salary) VALUES (%s, %s, %s, %s, %s)"""
cursor.execute(query, (1, "John Doe", 30, "IT", 50000))
connection.commit()
cursor.execute("SELECT * FROM employee")
data = cursor.fetchall()
print(data)
connection.close()