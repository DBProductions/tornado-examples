import tornado.web
import tornado.ioloop
import tornado.httpserver
from pymongo import Connection

MONGODBHOST = "localhost"
MONGODBPORT = 27017
DATABASE = "tornado"
COLLECTION = "user"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        docs = []
        user = self.application.db[COLLECTION]
        self.write("Tornado &amp; MongoDB (db:tornado, collection:user)<br>")
        for i in user.find():       
            self.write(i['name'] + "<br>")    

class Application(tornado.web.Application):
    def __init__(self):
        self.connection = Connection(MONGODBHOST, MONGODBPORT)
        self.db = self.connection[DATABASE]
        handlers = [(r".*", MainHandler)]
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
