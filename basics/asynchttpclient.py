import tornado.httpclient

def handle_response(response):
    if response.error:
        print "Error:", response.error
    else:
        print response.body
    tornado.ioloop.IOLoop.instance().stop()

http_client = tornado.httpclient.AsyncHTTPClient()
http_client.fetch("http://www.google.com/", handle_response)
tornado.ioloop.IOLoop.instance().start()