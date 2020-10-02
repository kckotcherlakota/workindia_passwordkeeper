

import pymysql

""" function to get database connection"""
def connect():
    DB_URI  = "localhost"
    DB_USER = "root"
    DB_PASS = ""
    DB_DATA = "password_manager"
    connection = pymysql.connect(DB_URI,DB_USER,DB_PASS,DB_DATA)
    return connection 

""" function to close active connection """
def close(cursor,conn):
    cursor.close()
    conn.close()    

