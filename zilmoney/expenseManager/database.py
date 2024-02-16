import mysql.connector


class DbServiceImpl:
    def dbConn(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'mydb'
        )

        return self.mydb
    
    def insert(user):
        query = "INSERT INTO expense"

    def findAll(tablename):
        try: 
            # db = Database()
            conn = DbServiceImpl.dbconnection()
            cur=conn.cursor()
            
            cur.execute("SELECT * FROM "+tablename)            
            rows = cur.fetchall()
            
            conn.commit()
            cur.close()
            return rows
        except Exception as error:
            print("DATA NOT SELECTED", str(error))
            if type(cur) is not str: cur.close()
        return False