import os
import sys
import logging
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route('/certificate', methods=["POST"])
def create_cert():
    domain = request.args.get('domain')
    result = os.system("bash /app/files/auto.sh " + domain)
    if result == 0:
        return make_response(jsonify({'status': "success"}), 200)

    return make_response(jsonify({'status': "failed"}), 400)


@app.route('/certificate', methods=["DELETE"])
def delete_cert():
    domain = request.args.get('domain')
    return 'Not Implemented yet!'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
    app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    app.logger.setLevel(logging.INFO)
