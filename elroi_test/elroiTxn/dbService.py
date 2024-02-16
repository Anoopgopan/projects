import pymongo
import logging
# logging.basicConfig()
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
class DbServiceImpl(object):
    def __init__(self,dbName):
        try:
            self.client = pymongo.MongoClient('mongodb://localhost:27017/')
            self.DATABASE = self.client[dbName]
        except Exception as e:
            logging.error("Exception ==> " + str(e))
        return None
    # INSERT DATA
    def insert(self,tableName,data):
        try:
            insert = self.DATABASE[tableName].insert_one(data)
            if not insert:
                return False
            return True
        except Exception as e:
            logging.error("Insert Exception ==> "+ str(e))
    #FIND ONE
    def findOne(self,tableName,query,filter):
        try:
            findData = self.DATABASE[tableName].find_one(query,filter)
            if not findData:
                return False
            return findData
        except Exception as e:
            logging.error("Insert Exception ==> "+ str(e))        
    # FETCHING DATA
    def find(self,tableName,query,filter):
        try:
            findData = list(self.DATABASE[tableName].find(query,filter))
            if not findData:
                return False
            return findData
        except Exception as e:
            logging.error("Insert Exception ==> "+ str(e))
    # UPDATE DATA    
    def update(self,tableName,condition,data):
        try:
            update = self.DATABASE[tableName].update_one(condition,{'$set':data})
        except Exception as e:
            logging.error("Insert Exception ==> "+ str(e))