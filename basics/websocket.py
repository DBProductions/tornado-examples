import os
import uuid
import tornado.web
import tornado.ioloop
import tornado.websocket
import tornado.httpserver

SOCKET_CLIENTS = []

class SocketHandler(tornado.websocket.WebSocketHandler):
    """ Handle the incoming sockets """
    def open(self):
        self.socket_id = str(uuid.uuid4())
        SOCKET_CLIENTS.append(self)
    def on_message(self, message):
        self.write_message(message)        
    def broadcast(self, message, this_not=None):
        for c in SOCKET_CLIENTS:
            c.write_message(message)
    def on_close(self):        
        SOCKET_CLIENTS.remove(self)
        self.broadcast('socket disconnected', self)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("websocket.html")

path = os.path.dirname(__file__)
tpl_path = os.path.join(path, "tmpl")
application = tornado.web.Application([(r"/", MainHandler),
                                       (r"/websocket", SocketHandler)],
                                      template_path=tpl_path)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
