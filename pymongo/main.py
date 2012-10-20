import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
import os
from pymongo import Connection

define("port", default=8888, help="Run server on a specific port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        connection = Connection('localhost', 27017)
        db = connection.tornado
        user = db.user
        logging.info( db.collection_names() )
        docs = []
        for i in user.find():
            docs.append(i)       
        self.render("index.html", docs=docs)      
        
local_static_path = os.path.join(os.path.dirname(__file__), "static")

application = tornado.web.Application([(r".*", MainHandler)],static_path=local_static_path)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    tornado.options.parse_command_line()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
