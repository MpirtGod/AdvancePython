import json
from urllib.parse import parse_qsl


def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'application/json')]
    path = environ.get('PATH_INFO', '').lstrip('/')
    query = environ.get('QUERY_STRING', '')
    params = dict(parse_qsl(query))
    response_body = {}

    if path == 'hello':
        if 'user' in params:
            response_body['message'] = f"Hello, {params['user']}!"
        else:
            response_body['message'] = "Hello, world!"
    else:
        status = '404 Not Found'
        response_body['error'] = "Page not found"

    response_body = json.dumps(response_body).encode('utf-8')
    content_length = len(response_body)
    headers.append(('Content-Length', str(content_length)))

    start_response(status, headers)
    return [response_body]