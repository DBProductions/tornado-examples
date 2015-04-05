import tornado.httpserver
import tornado.ioloop
import tornado.web
import motor

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        db = self.settings['db']
        db.user.find().sort([('_id', -1)]).each(self.receive_message)
    def receive_message(self, message, error):
        if error:
            raise tornado.web.HTTPError(500, error)
        elif message:
            self.write('<div>%s</div>' % message)
        else:
            # Iteration complete
            self.finish()

db = motor.MotorClient().tornado

application = tornado.web.Application([(r'/', MainHandler)], db=db)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()