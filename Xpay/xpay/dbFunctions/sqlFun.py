import mysql.connector
import logging
from mysql.connector import Error
# from pydantic import BaseModel
from multiprocessing.pool import CLOSE

logging.basicConfig()
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


class Database():
    def dbconnection(self):
        self.mydb = mysql.connector.connect(
                    host = "localhost",
                    user  = "root",
                    password = "1234",
                    database = "mydb"
                )
        return self.mydb




# class User(BaseModel):
#     id: str
#     name: str
#     mobile : str
#     email: str
#     password : str
#     profile : str

class userInsert:
    def insertUserdb(user):
        logging.info("Insertion data === " + str(user))
        query = "INSERT INTO user(id,name, mobile,email,password) VALUES (%s, %s,%s,%s,%s)"
        try:
            db = Database()
            connection = db.dbconnection()
            cursor = connection.cursor()
            cursor.execute(query, user)
            connection.commit()
            cursor.close()
            return {"message": "Item created successfully"}
        except Error as e:
            print(f"The error '{e}' occurred")
            return {"message": "Error occurred while creating the item"}

    def insertProfile(profile):
        logging.info("Insertion data === " + str(profile))
        query = "INSERT INTO user(id,profile_pic) VALUES (%s,%s)"
        try:
            db = Database()
            connection = db.dbconnection()
            cursor = connection.cursor()
            cursor.execute(query, profile)
            connection.commit()
            cursor.close()
            return {"message": "Item created successfully"}
        except Error as e:
            print(f"The error '{e}' occurred")
            return {"message": "Error occurred while creating the item"}
        
    def findOne(tablename,query):
        logging.info("Find ::==>>" + str(query))
        try: 
            db = Database()
            conn = db.dbconnection()
            cur=conn.cursor()
            
            if type(query[1]) is int:
                cur.execute("SELECT * FROM "+tablename+" WHERE {} = {}".format(query[0], query[1]))
            else:
                cur.execute("SELECT * FROM "+tablename+" WHERE {} = '{}'".format(query[0], query[1]))            
            rows = cur.fetchall()
            conn.commit()
            cur.close()
            return rows
        except Exception as error:
            logging.info("DATA NOT SELECTED" + str(error))
            if type(cur) is not str: cur.close()
        return False    
    
    def findAll(tablename):
        try: 
            db = Database()
            conn = db.dbconnection()
            cur=conn.cursor()
            
            cur.execute("SELECT * FROM "+tablename)            
            rows = cur.fetchall()
            
            conn.commit()
            cur.close()
            return rows
        except Exception as error:
            logging.info("DATA NOT SELECTED" + str(error))
            if type(cur) is not str: cur.close()
        return False