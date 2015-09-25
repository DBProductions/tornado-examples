#!/usr/bin/env python
""" application class example """

import tornado.ioloop
import tornado.web

PORT = 8888

class MainHandler(tornado.web.RequestHandler):
    """ main request handler """
    def get(self):
        message = "You requested %s\n" % self.request.uri
        self.write(message)

class Application(tornado.web.Application):
    """" application class """
    def __init__(self):
        handlers = [(r".*", MainHandler)]
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    Application().listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
