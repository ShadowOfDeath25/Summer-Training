import mysql.connector as db
import os


def connect_db():
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASS']
    mydb = db.connect(host='localhost',
                      username=db_user,
                      password=db_pass,
                      database='autoshop')
    return mydb


