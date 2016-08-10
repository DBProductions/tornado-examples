#!/usr/bin/env python
""" asynchronous http proxy """

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.httpclient

client = tornado.httpclient.AsyncHTTPClient(max_clients=1000)

class Handler(tornado.web.RequestHandler):
    def callback(self, resp):
        try:
            self.write('got resp: %s status, %s len' % (resp.code, len(resp.body)))
        finally:
            self.finish()

    @tornado.web.asynchronous
    def get(self):
        req = tornado.httpclient.HTTPRequest('http://www.google.com/search?q=ddos')
        client.fetch(req, self.callback)

application = tornado.web.Application([(r'/', Handler)])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
