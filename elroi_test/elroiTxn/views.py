from flask import Flask
from flask import request
from elroiTxn import app
from elroiTxn.service import TransactionServiceImpl


@app.route('/')
def default():
    return "ELROI TRANSACTION SERVER IS RUNNING...!!!"

# request format
# {
#   "AccNo":"1234566788",
#   "loadamount":"1000.00",
#   "type":"LOAD"
# }
@app.route('/cardTransaction',methods = ['POST'])
def loadMoney():
    result = TransactionServiceImpl.cardTransaction(request.data)
    return result
# {
#   "AccNo":"1234566788"
# }
@app.route('/statement',methods=['POST'])
def miniStatement():
    return TransactionServiceImpl.ministatements(request.data)