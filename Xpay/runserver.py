from os import environ
from xpay import app
import uvicorn
import tracemalloc


if __name__ == '__main__':
    tracemalloc.start()
    uvicorn.run(app, host="localhost", port=8000)