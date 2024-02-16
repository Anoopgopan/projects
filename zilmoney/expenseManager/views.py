from expenseManager import app
from pydantic import BaseModel
from fastapi import FastAPI

from expenseManager.database import DbServiceImpl


app = FastAPI()

class Expense(BaseModel):
    name : str
    amount : float
    category : str


@app.get('/')
def root():
    return "Running...!!!"

expenseList = []
@app.post('POST/expense')
def add_expense(expense:Expense):
    print("==================>>>")
    expensedata = expense.model_dump()
    expenseList.append(expensedata)
    DbServiceImpl.insert(expense.name,
                         expense.amount,
                         expense.category)
    return {"message":"Successfully inserted"}


@app.get('/GET/expenses')
def get_all_expense():

    expData= DbServiceImpl.findAll("expense")
    if not expData:
        return {"message":"user not found"}
    return {"message":expData}


@app.get('/GET /expenses/month/{year}/{month}')
def fetchall_monthly_exp():
    resp = {
        "expense":[]
    }
    return resp

# @app.get('/GET/totals/')
# def get_total():
    