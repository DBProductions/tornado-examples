import tornado.httpserver
import tornado.ioloop
import tornado.web
from pymongo import Connection

connection = Connection('localhost', 27017)
db = connection.tornado
user = db.user

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        docs = []
        self.write("tornado &amp; mongo (db:tornado, collection:user)<br>")
        for i in user.find():       
            self.write(i['name'] + "<br>")    

application = tornado.web.Application([(r".*", MainHandler)])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
