#!/usr/bin/env python
""" blocking HTTP client example """

import tornado.httpclient

URL = "http://www.google.com/"

http_client = tornado.httpclient.HTTPClient()

try:
    response = http_client.fetch(URL)
    print response.body
except tornado.httpclient.HTTPError, e:
    print "Error:", e
