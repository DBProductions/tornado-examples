import tornado.httpserver
import tornado.ioloop
import tornado.web
import redis

REDISHOST = "localhost"
REDISPORT = 6379

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.application.r.set('key', 'Redis')
        value = self.application.r.get('key')
        self.write("Tornado &amp; " + value)      
      
class Application(tornado.web.Application):
    def __init__(self):
        self.r = redis.Redis(host=REDISHOST, port=REDISPORT, db=0)
        handlers = [(r".*", MainHandler)]
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()