import tornado.web
import tornado.ioloop
from tornado.options import define, options

define("port", default=8888, help="application port", type=int)

class MainHandler(tornado.web.RequestHandler):
    """ main request handler """
    def get(self):
        message = "You requested %s\n" % self.request.uri
        self.set_header("Content-Type", "text/plain")    
        self.write(message)

class JsonHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def convertReqBody(self, body):
        data = {}
        try:
            data = json.loads(body)
        except ValueError:
            elements = urllib.unquote_plus(body).split("&")
            for i in elements:
                couple = i.split("=")
                if len(couple) > 1:
                    data[couple[0]] = couple[1]
        return data

    def get(self):
        self.write({"response": "GET", "uri": self.request.uri})

    def post(self):
    	data = self.convertReqBody(self.request.body)
    	data['timestamp'] = int(time.time())
    	self.write({"response": "POST", "uri": self.request.uri, "data": data})

class Application(tornado.web.Application):
    """" application class """
    def __init__(self):
        handlers = [(r"/json.*", JsonHandler),
                    (r".*", MainHandler)]
        settings = {
            "debug": True,
            "autoreload": True,
            "compress_response": True,
            "cookie_secret": "secret123"
        }
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
