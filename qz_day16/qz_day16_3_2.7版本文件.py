# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang

# 在2.7版本下

from wsgiref.simple_server import make_server


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    return 'oldboy 123'


if __name__ == '__main__':
    httpd = make_server('', 8001, RunServer)
    print "Serving HTTP on port 8001..."
    httpd.serve_forever()
