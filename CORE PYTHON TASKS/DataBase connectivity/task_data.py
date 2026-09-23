import pymysql


def insertLogin():
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='login'
    )

    cursor1 = connection.cursor()

    cursor1.execute(
        "insert into login(id, fn, ln, un, pwd) values (%s, %s, %s, %s, %s)",
        (1, 'John', 'Doe', 'johndoe', 'password123')
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM login")
    data = cursor.fetchall()
    print(data)
    print("Data fetched successfully")
    connection.commit()


insertLogin()