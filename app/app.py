import os
import sys
import logging
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/certificate', methods=["POST"])
def create_cert():
    try:
        print("Oops!  That was no valid number.  Try again...")
        domain = request.args.get('domain')
        result = os.system("bash /app/files/auto.sh " + domain)
        if result == 0:
            return make_response(jsonify({'status': "success"}), 200)
    except RuntimeError:
        return make_response(jsonify({'status': "failed"}), 400)


@app.route('/certificate', methods=["DELETE"])
def delete_cert():
    domain = request.args.get('domain')
    return 'Not Implemented yet!'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
    app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    app.logger.setLevel(logging.INFO)
