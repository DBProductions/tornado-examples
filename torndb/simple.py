import tornado.httpserver
import tornado.ioloop
import tornado.web
import torndb

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Tornado &amp; Torndb (MySQL)<br>")
        for i in self.application.db.query("SELECT * FROM user"):
            self.write(i.name + '<br>');
        self.application.db.close();       

class Application(tornado.web.Application):
    def __init__(self):
        self.db = torndb.Connection("localhost", "tornado", "root", "admin")
        handlers = [(r".*", MainHandler)]
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()