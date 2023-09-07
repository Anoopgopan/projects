import pymongo
import logging


logging.basicConfig()
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


class MongoDbServiceImpl(object):
    URI = 'localhost'
    USER = 'mydb'
    PASS = None
    DATABASE = None


    def __init__(self,dbName):
        try:
            self.client = pymongo.MongoClient(MongoDbServiceImpl.URI,username=MongoDbServiceImpl.USER,password=MongoDbServiceImpl.PASS)
            self.DATABASE = self.client[dbName]
        except pymongo.errors.PyMongoError as e:
            logging.error("Error Mongo"+str(e))
        except pymongo.errors.ConnectionFailure as e:
            logging.error("Connection Error "+str(e))
        except pymongo.errors.ServerSelectionTimeoutError as e:
            logging.error("Server Selection Error "+str(e))
        except Exception as e:
            logging.error("EXCEPTION "+str(e))
        return None

    # 1. FIND ONE 
    def findOne(self,tb_name,query,filter) :
        try:
            data =  self.DATABASE[tb_name].find_one(query, filter)
            if not data:
                return False
        except Exception as e:
            logging.error(str(tb_name)+' '+str(query)+' '+str(filter)+" EXCEPTION AT FIND DB "+str(e))
            data = False
        return data
    
    # 2. FIND ALL
    def findAll(self,tb_name,query,filter) :
        try:
            allData = list(self.DATABASE[tb_name].find(query, filter))
            if not allData:
                return False
        except Exception as e:
            logging.error(str(tb_name)+' '+str(query)+' '+str(filter)+" EXCEPTION AT FIND ALL DB "+str(e))
            allData = False
        return allData
    
    # 3 .INSERT ONE
    def insertOne(self,tb_name,dataDict):
        try:
            insertRes =  self.DATABASE[tb_name].insert_one(dataDict)
            if insertRes:   
                return True
            else:
                return False
        except Exception as e:
            logging.error(str(tb_name)+' '+str(dataDict)+" EXCEPTION AT INSERTION DB "+str(e))
            return False

