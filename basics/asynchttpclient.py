#!/usr/bin/env python
""" non-blocking HTTP client example """

import tornado.httpclient

URL = "http://www.google.com/"

def handle_response(response):
    """ request handler function """
    if response.error:
        print "Error:", response.error
    else:
        print response.body
    tornado.ioloop.IOLoop.instance().stop()

client = tornado.httpclient.AsyncHTTPClient()
client.fetch(URL, handle_response)
tornado.ioloop.IOLoop.instance().start()
