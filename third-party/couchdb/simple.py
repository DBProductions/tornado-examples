import tornado.httpserver
import tornado.ioloop
import tornado.web
import httplib

COUCHHOST = "127.0.0.1"
COUCHPORT = 5984

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        connection = httplib.HTTPConnection(COUCHHOST, COUCHPORT)
        connection.request("GET", "/tornado/doc_id")
        res = connection.getresponse()
        doc = res.read()
        self.write("tornado &amp; couchdb<br>")
        self.write(doc)
        
application = tornado.web.Application([(r".*", MainHandler)])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
