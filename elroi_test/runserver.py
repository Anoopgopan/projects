from elroiTxn import app
from os import environ


if __name__ == '__main__':
    app.run('127.0.0.1',5000,debug=True)