import os
from flask import Flask, request, jsonify, url_for
import json

app = Flask(__name__)

# Simple endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'hello'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
