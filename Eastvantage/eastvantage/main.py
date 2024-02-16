# from os import environ
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message":"Running...!!!"}