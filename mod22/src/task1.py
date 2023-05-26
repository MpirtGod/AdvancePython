import json
import time
from flask import Flask, jsonify

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'application/json')]
    path = environ.get('PATH_INFO', '').strip('/').split('/')
    response_body = {}

    if path[0] == 'hello':
        if len(path) == 2:
            response_body['message'] = f"Hello, {path[1]}!"
        else:
            response_body['message'] = "Hello, world!"
    else:
        status = '404 Not Found'
        response_body['error'] = f"Page not found"

    response_body = json.dumps(response_body).encode('UTF-8')

    start_response(status, headers)
    return [response_body]


app = Flask(__name__)


@app.route('/long_task')
def long_task():
    time.sleep(300)
    return jsonify(message='We did it!')
