from dbconfig import connect,close
import pymysql


class Account:

    tablename = "Account"
    
    ''' function to get accounts of a user '''
    @classmethod
    def getByUserId(cls,user_id):
        try:
            conn   = connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor) 
            query = "SELECT * FROM {} WHERE `user_id`={}".format(cls.tablename,user_id)
            cursor.execute(query)
            res = cursor.fetchall()
            return res
        except Exception as e:
            print(e)
            return None 
        finally:
            close(cursor,conn)

    '''function to save a new account'''
    @classmethod
    def save(cls,data):
        try:
            conn = connect()
            cursor = conn.cursor()
            query  = "INSERT INTO {}(`user_id`,`website`,`username`,`password`) VALUES(%s,%s,%s,%s)".format(cls.tablename)
            bind   = (data["user"],data["website"],data["username"],data["password"])
            cursor.execute(query,bind)
            conn.commit()

            return True
        except Exception as e:
            print(e)
            return False 
        finally:
            close(cursor,conn)        
