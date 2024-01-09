#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

@Request.application
def application(response):
    print(f'This web server is running at {request.remote_addr}')
    return('A WSGI generated this response! and i love how i am flowing. Thankyou God')
    
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )

