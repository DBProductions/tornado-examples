import tornado.ioloop
import tornado.web
import sockjs.tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class EchoConnection(sockjs.tornado.SockJSConnection):
    participants = set()
    def on_open(self, info):
        self.broadcast(self.participants, "Someone joined.")
        self.participants.add(self)
    def on_message(self, message):
        self.broadcast(self.participants, message)
    def on_close(self):
        self.participants.remove(self)
        self.broadcast(self.participants, "Someone left.")

if __name__ == "__main__":
    EchoRouter = sockjs.tornado.SockJSRouter(EchoConnection, '/echo')
    app = tornado.web.Application([(r"/", MainHandler)] + EchoRouter.urls)
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
