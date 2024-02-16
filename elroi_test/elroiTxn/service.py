import json
import logging
import csv
import datetime

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
from elroiTxn.dbService import DbServiceImpl
elroi = DbServiceImpl('elroi')
class TransactionServiceImpl:
    def cardTransaction(request):
        req = json.loads(request.decode('utf-8'))
        logging.info("Request from UI ==> " + str(req))
        try:
            #load amount to card ==> Cr
            print("type===>",req['type'])
            if req['type'] == "LOAD":
                id = elroi.findOne('users',{'AccNo':req['AccNo']},{'_id':0})
                print(id)
                # update user amount and insert into transactions
                loadamt = float(id['CurrentBal']) + float(req['loadamount'])
                print("load amount==>",loadamt)
                
                update_bal = elroi.update('users',{'AccNo':req['AccNo']},{'CurrentBal':loadamt})

                print("update==>",update_bal)
                insertdata ={
                    "Id": int(id['Id']),
                    "AccNo": req['AccNo'],
                    "subTxnType": "Cr",
                    "timeStamp": str(datetime.datetime.now()),
                    "amount": float(loadamt)

                }
                print("==>",insertdata)
                txnins = elroi.insert('transactions',insertdata)
                print("------------------------------")
            else:

                id = elroi.findOne('users',{'AccNo':req['AccNo']},{'_id':0})

                # update user amount and insert into transactions
                loadamt = float(req['CurrentBal']) - float(id['loadamount'])
                update_bal = elroi.update('users',{'AccNo':req['AccNo']},{'CurrentBal':loadamt})

       
                insertdata ={
                    "Id": int(id['ID']),
                    "AccNo": req['AccNo'],
                    "subTxnType": "Dr",
                    "timeStamp": str(datetime.datetime.now()),
                    "amount": float(loadamt)

                }
                txnins = elroi.insert('transactions',insertdata)
                
                id = elroi.findOne('users',{'AccNo':req['AccNo']},{'_id':0})

            return id

        except Exception as e:
            logging.error("Exception ==> " + str(e) )


    def ministatements(request):
        req = json.loads(request.decode('utf-8'))
        logging.info("Request from UI ==> " + str(req))
        try:
            transactions = elroi.find('transactions',req,{'_id':0})
            print(transactions)

            stmnts =[]
            bal = 0
            for data in transactions:
                if data['subTxnType']=="Cr":
                    debit = "0.00"
                    credit = data['amount']
                    bal = float(bal) + float(data['amount'])

                else:
                    debit = data['amount']
                    credit = "0.00"
                    bal = float(bal) - float(data['amount'])

                
                miniList = [data['timeStamp'],debit,credit,bal]

                stmnts.append(miniList)
                head = ['Date','debit','Credit','Balance']

                csv_file = [head]+ stmnts
                print(csv_file)

                file_name ="mini_statement.csv"
                with open(file_name,'w') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerows(csv_file)
            return stmnts
        except Exception as e:
            logging.error("Exception ==> " + str(e) )