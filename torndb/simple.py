import tornado.httpserver
import tornado.ioloop
import tornado.web
import torndb

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Tornado &amp; Torndb (MySQL)<br>")
        db = torndb.Connection("localhost", "tornado", "root", "admin")
        for i in db.query("SELECT * FROM user"):
            self.write(i.name + '<br>');
        db.close();       

application = tornado.web.Application([(r".*", MainHandler)])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
