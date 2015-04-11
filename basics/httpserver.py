#!/usr/bin/env python
#
# A non-blocking, single-threaded HTTP server

import tornado.httpserver
import tornado.ioloop

def handle_request(request):
    message = "You requested %s\n" % request.uri
    request.write("HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % (len(message), message))
    request.finish()

http_server = tornado.httpserver.HTTPServer(handle_request)
http_server.listen(8888)
tornado.ioloop.IOLoop.instance().start()
