import mysql.connector as db
import os


def connect_db():
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASS']
    mydb = db.connect(host='localhost',
                      username=db_user,
                      password=db_pass,
                      port=3306,
                      database='autoshop')
    return mydb


#curr_db = connect_db()
#cursor = curr_db.cursor()
#val = cursor.execute('SELECT * FROM users')
#cursor.fetchall()
#for row in val:
 #   print(row)