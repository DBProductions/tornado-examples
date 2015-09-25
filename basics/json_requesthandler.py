#!/usr/bin/env python

import json
import time
import urllib
import tornado.ioloop
import tornado.web

PORT = 8888

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

application = tornado.web.Application([(r".*", JsonHandler)], debug=True, autoreload=True)

if __name__ == "__main__":
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
