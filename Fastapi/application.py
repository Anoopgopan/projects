from fastapi import FastAPI
from pydantic import BaseModel
from database import expenses

app = FastAPI()

class Expense(BaseModel):
    name:str
    amount:float
    category:str

expenseList = []

@app.post("/add/expenses")
def add_expense(expense:Expense):
    expenseEntry = expense.model_dump()
    expenseList.append(expenseEntry)
    expenses.insert().values(expense.model_dump())
    
    # name = expense.get("name")
    # amount = expense.get("amount")
    # category = expense.get("category")

    resp = {
        "message":"Expense added successfully",
        "name":expense.name
    }
    return resp



@app.get("/get/expenses/")
def fetch_expense_month():
    
    resp = {
        "expenses":[]
    }
    return resp



@app.get("/get/expenses/month/{year}/{month}/")
def fetch_expense_month(year:str, month:str):
    
    resp = {
        "expenses":[],
        "name":""
    }
    return resp