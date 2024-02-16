from os import environ
import uvicorn
from expenseManager import app
import tracemalloc

if __name__ == "__main__":
    tracemalloc.start()
    uvicorn.run(app,host ='localhost',port =8000)
