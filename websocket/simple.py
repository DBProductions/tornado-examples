#!/usr/bin/env python

import uuid
import tornado.web
import tornado.ioloop
import tornado.websocket
import tornado.httpserver

class SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.socket_id = str(uuid.uuid4())
        print "WebSocket opened", self.socket_id
    def on_message(self, message):
        print self.socket_id, "send message"
        self.write_message(message)
    def on_close(self):
        print "WebSocket closed"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

application = tornado.web.Application([(r"/", MainHandler),
                                       (r"/websocket", SocketHandler)])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
