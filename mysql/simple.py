import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.database

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Tornado &amp; MySQL")
        db = tornado.database.Connection("localhost", "tornado", "root", "")
        for i in db.query("SELECT * FROM user"):
            self.write(i.name);
        db.close();       

application = tornado.web.Application([(r".*", MainHandler)])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
