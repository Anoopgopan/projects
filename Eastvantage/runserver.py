from os import environ
import uvicorn
import tracemalloc
from eastvantage import app

if __name__ == '__main__':
    tracemalloc.start()
    uvicorn.run(app, host ="localhost", port=5000)

