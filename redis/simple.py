import tornado.httpserver
import tornado.ioloop
import tornado.web
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        r.set('key', 'redis')
        value = r.get('key')
        self.write("tornado " + value)      
        
application = tornado.web.Application([(r".*", MainHandler)])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()