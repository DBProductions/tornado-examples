import tornado.httpserver
import tornado.ioloop
import tornado.web
from neo4jrestclient.client import GraphDatabase

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        nodeid = self.get_argument('id', 1)
        node = self.application.gdb.node[nodeid]
        rel = []
        for i in node.relationships.all():
            rel.append(i)
        self.render("index.html", node=node, rel=rel)

class Application(tornado.web.Application):
    def __init__(self):
        self.gdb = GraphDatabase("http://localhost:7474/db/data/")
        handlers = [(r".*", MainHandler)]
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()