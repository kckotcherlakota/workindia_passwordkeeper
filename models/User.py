from dbconfig import connect,close
import pymysql
from werkzeug.security import generate_password_hash

""" User Entity """
class User:

    tablename = "User"
    def __init__(self,id,username,password):
        self.id = id
        self.username = username 
        self.password = password 


    """ function to find a user by username """
    @classmethod
    def find_by_username(cls,username):
        try:
            conn  = connect()
            query = 'SELECT * FROM {} WHERE `username`="{}"'.format(cls.tablename,username)
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            res = cursor.fetchone()
            return res 
        except Exception as e:
            print(e)
            return None 
        finally:
            close(cursor,conn)

    @classmethod
    def save(cls,data):
        try:
            conn = connect()
            cursor = conn.cursor()
            query = "INSERT INTO {}(`username`,`password`) VALUES(%s,%s)".format(cls.tablename)
            #generate password hash
            pass_hash = generate_password_hash(data["password"])
            bind  = (data["username"],pass_hash)
            cursor.execute(query,bind)
            conn.commit()
            return True

        except Exception as e:
            print(e)
            return False
        finally:
            close(cursor,conn)                  

