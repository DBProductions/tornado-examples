import tornado.httpserver
import tornado.ioloop
import tornado.web
import os

class HeadlineModule(tornado.web.UIModule):
    def render(self, title):
        return '<h1>' + title + '</h1>'
    
class MainHandler(tornado.web.RequestHandler):
    def get(self):        
        self.render("index.html", content="Lorem ipsum...")
        
tpl_path = os.path.join(os.path.dirname(__file__), "tmpl")

application = tornado.web.Application([(r".*", MainHandler)], 
                                      template_path=tpl_path,
                                      ui_modules={'Headline':HeadlineModule})

if __name__ == "__main__":
    http_server= tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    