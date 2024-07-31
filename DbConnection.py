import mysql.connector as db
import os


def connect_db():
    db_user = os.environ['db_user']
    db_pass = os.environ['db_pass']
    mydb = db.connect(host='localhost',
                      username='root',
                      password='mo992004')
    return mydb
