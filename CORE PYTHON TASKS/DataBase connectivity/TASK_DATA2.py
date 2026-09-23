import pymysql


def insertLogin():
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='userlogin'
    )

    cursor1 = connection.cursor()

    cursor1.execute(
        "insert into userlogin(id, first_name, last_name, username, pass, course) values (%s, %s, %s, %s, %s, %s)",
        (41, 'YASH', 'Suthar', 'yash1234', 12345, 'IT')
    )
    cursor1.execute(
        "insert into userlogin(id, first_name, last_name, username, pass, course) values (%s, %s, %s, %s, %s, %s)",
        (157, 'baku', 'DFG', 'baku1234', 22277, 'CSE')
    )
    cursor1.execute(
        "insert into userlogin(id, first_name, last_name, username, pass, course) values (%s, %s, %s, %s, %s, %s)",
        (557, 'DKFS', 'DSDF', 'KDJN1234', 22877, 'ITA')
    )
    cursor = connection.cursor()  
    cursor.execute("SELECT * FROM userlogin")
    cursor.execute("delete from userlogin where id= 41")
    data = cursor.fetchall()
    print(data)
    print("Data fetched successfully")
    connection.commit()


insertLogin()