import redis
import tornado.web
import tornado.ioloop
import tornado.httpserver

REDISHOST = "localhost"
REDISPORT = 6379
REDISDB = 0

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.application.r.set('key', 'Redis')
        value = self.application.r.get('key')
        self.write("Tornado &amp; {}".format(value.decode('utf-8')))

class Application(tornado.web.Application):
    def __init__(self):
        self.r = redis.Redis(host=REDISHOST, port=REDISPORT, db=REDISDB)
        handlers = [(r".*", MainHandler)]
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()