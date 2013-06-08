import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket

class SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"
    def on_message(self, message):
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
