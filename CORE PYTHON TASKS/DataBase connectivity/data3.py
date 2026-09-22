import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db = "employee"
)
#cursor = connection.cursor()
#query = """INSERT INTO employee (name,age, department, salary) VALUES (%s, %s, %s, %s)"""
#cursor.execute(query, ("John Doe", 30, "IT", 50000))
#connection.commit()
#connection.close()