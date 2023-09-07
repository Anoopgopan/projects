from xpay import app
from xpay.dbFunctions.mongoDbFun import MongoDbServiceImpl
import logging



logging.basicConfig()
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

xpay_db = MongoDbServiceImpl('xpay_db')


@app.get("/")
def root():
    return "Xpay Service is Running.......!!!!"


# ::::::::::::::: MONGO DB FUNCTIONS  :::::::::::::::::::::::::

# User registration :: Insert into DB

@app.post("/mongo/registration")
async def mongoRegistration(value: dict):
    logging.info("Incoming Request ==== " + str(value))
    
    # insert incoming request into mongodb
    # Password is encrypted
    # UI encrypted the profile pic into url 
    
    id = xpay_db.findAll('user',{},{'_id':0})
    
    if id:
        last_id_find =  list(map(lambda x : x['id'], id))
        # logging.info("Id List is ::::::::  " + str(last_id_find))
        sort = sorted(last_id_find)
        
        # logging.info("Sorted List is :::::: " + str(sort))
        logging.info("Last Element is ::::: " + str(sort[-1]))

        last_id = int(sort[-1]) + 1
    else:
        last_id = 1
    
    logging.info("Insertion Id :::::: " + str(last_id))

    user_data = {
        "id": str(last_id),
        "name":value['full_name'],
        "email":value['email'],
        "password":value['password'],
        "mobile":value['phone']
        }
    
    profile_data = {
        "id":str(last_id),
        "pic": value['profile_picture']
    }

    logging.info("user insertion data ===== " + str(user_data))
    logging.info("profile insertion data == " + str(profile_data))
    # logging.info("Insertion Data === " + str(data))
    
    insert_user = xpay_db.insertOne('user',user_data)
    insert_profile = xpay_db.insertOne("profile",profile_data)
    
    if not insert_user and insert_profile:
        return {"message":"Fail to insert"}
    
    return {"message": "Successfully Inserted"}

# Check email already Exist

@app.post("/mongo/check/email")
async def mongoCheckEmail(value: dict):
    logging.info("Incoming Request ==== " + str(value))

    searchEmail = xpay_db.findOne('user',{'email':value['email']},{'_id':0})
    logging.info("Response === " + str(searchEmail))
    if not searchEmail:
        return {"message":"Email Not Found"}
    return {"message":"Email already Exist"}

# Get all customer List

@app.get("/mongo/get/users")
async def mongoGetUser():
    users = xpay_db.findAll('user',{},{'_id':0,'id':1,'name':1})
    logging.info("Response === " + str(users))
    if not users:
        return {"message":"User Not Found"}
    return {"message" :users}

#::::::::::::::::::::::: SQL FUNCTIONS :::::::::::::::::::::::::::::::::

from xpay.dbFunctions.sqlFun import Database,userInsert

@app.post("/sql/registration")
def insertUser(user: dict):
    logging.info("Incoming data === " + str(user))

    userInsert.insertUserdb((user['name'],
                            user['phone'],
                            user['email'],
                            user['password']))
    
    return {'message':'successfully inserted'}
    
@app.post("/sql/insert/profile")
def insertProfile(profile:dict):
    logging.info("Incoming data === " + str(profile))

    userInsert.insertProfile((profile['id'],
                              profile['profile_picture']))
    return {'message':'successfully inserted'}

# Check email already Exist
@app.post("/sql/check/email")
def insertProfile(data:dict):
    logging.info("Incoming data === " + str(data))
    
    details= userInsert.findOne("user",['email',data['email']])
    if not details:
        return {"message":"email not found"}  
    return {'message':'Email alrady exist'}

# list all customers
@app.post("/sql/list/customers")
def listAllCustomers(customers:dict):
    logging.info("Incoming request === " + str(customers))

    custData= userInsert.findAll("user")
    if not custData:
        return {"message":"user not found"}
    return {"message":custData}