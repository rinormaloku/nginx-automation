import sys
import logging
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/create/cert')
def create_cert():
    return 'Certificate Created!'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
    app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    app.logger.setLevel(logging.INFO)
