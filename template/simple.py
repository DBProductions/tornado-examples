#!/usr/bin/env python

import os
import tornado.web
import tornado.ioloop
import tornado.template
import tornado.httpserver

class HeadlineModule(tornado.web.UIModule):
    def render(self, title):
        return "<h1>" + title + "</h1>"

class FooterModule(tornado.web.UIModule):
    def render(self, value):
        t = tornado.template.Template("<span>{{ msg }}</span>")
        return t.generate(msg=value)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",
                    page_title="Template",
                    content="Handling templates with Tornado.")

path = os.path.dirname(__file__)
tpl_path = os.path.join(path, "tmpl")
static_path = os.path.join(path, "static")

application = tornado.web.Application([(r".*", MainHandler)],
                                      template_path=tpl_path,
                                      static_path=static_path,
                                      ui_modules={"Headline":HeadlineModule,
                                                  "Footer":FooterModule})

if __name__ == "__main__":
    http_server= tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
