import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
import os, httplib, pycurl, StringIO

define("port", default=8888, help="Run server on a specific port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info("Request to MainHandler with pymongo")
        # httplib 
        connection = httplib.HTTPConnection('127.0.0.1', 5984)
        connection.request("GET", "/tornado/cats")
        res = connection.getresponse()
        data = res.read()
        docs = [res.status, res.reason, data]
        # pycurl 
        c = pycurl.Curl()
        c.setopt(pycurl.URL, "127.0.0.1:5984")
        c.setopt(pycurl.HTTPHEADER, ["Accept:"])
        b = StringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.MAXREDIRS, 5)
        c.perform()
        docs = [b.getvalue()]
        # output      
        self.render("index.html", docs=docs)      
        
local_static_path = os.path.join(os.path.dirname(__file__), "static")

application = tornado.web.Application([(r".*", MainHandler)],static_path=local_static_path)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    tornado.options.parse_command_line()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
