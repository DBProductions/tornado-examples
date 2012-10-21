import tornado.httpclient

http_client = tornado.httpclient.HTTPClient()

try:
    response = http_client.fetch("http://www.google.com/")
    print response.body
except tornado.httpclient.HTTPError, e:
    print "Error:", e