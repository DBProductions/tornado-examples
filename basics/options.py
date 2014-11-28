# python options.py -port=8880

import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define, options
define("port", default=8888, help="run on given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/plain")
        self.write("tornado response")

application = tornado.web.Application([(r"/", MainHandler)])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
