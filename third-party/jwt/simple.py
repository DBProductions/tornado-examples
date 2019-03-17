import jwt
import tornado.web
import tornado.ioloop
import tornado.httpserver

TOKENSECRET = 'asd&*&9798ashdkas#%$*&8jhHKHjhakjhdaksjdasdasd'

class TokenHandler(tornado.web.RequestHandler):
    def get(self):
        token = self.get_argument('token', '')
        decoded = jwt.decode(token, TOKENSECRET, algorithms=['HS256'])
        self.write(decoded)
    def post(self):
        name = self.get_argument('name')
        encoded = jwt.encode({'name': name}, TOKENSECRET, algorithm='HS256')
        self.write(encoded)

application = tornado.web.Application([(r'/', TokenHandler)])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()