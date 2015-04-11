#!/usr/bin/env python

import tornado.web
import tornado.ioloop
import tornado.httpserver
from pymongo import Connection

MONGODBHOST = "localhost"
MONGODBPORT = 27017

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        docs = []
        user = self.application.db.user
        self.write("tornado &amp; mongo (db:tornado, collection:user)<br>")
        for i in user.find():       
            self.write(i['name'] + "<br>")    

class Application(tornado.web.Application):
    def __init__(self):
    	self.connection = Connection(MONGODBHOST, MONGODBPORT)
        self.db = self.connection.tornado
        handlers = [(r".*", MainHandler)]
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
