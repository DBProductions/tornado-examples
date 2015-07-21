#!/usr/bin/env python

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):        
    def get(self):
        message = "You requested %s\n" % self.request.uri
        self.write(message)

application = tornado.web.Application([(r".*", MainHandler)], debug=True, autoreload=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
