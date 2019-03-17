import tornado.httpclient

URL = "http://www.dbproductions.de/"

def http_request():
    http_client = tornado.httpclient.HTTPClient()
    try:
        response = http_client.fetch(URL)
    except Exception as e:
        print("Error: %s" % e)
    else:
        print("Status Code: {}, Request Time: {}, Body Length: {}".format(response.code,
                                                                          response.request_time,
                                                                          len(response.body)))

async def async_http_request():
    http_client = tornado.httpclient.AsyncHTTPClient()
    try:
        response = await http_client.fetch(URL)
    except Exception as e:
        print("Error: %s" % e)
    else:
        print("Status Code: {}, Request Time: {}, Body Length: {}".format(response.code,
                                                                          response.request_time,
                                                                          len(response.body)))

# do a synchronous http request
http_request()
# do a asynchronous http request
tornado.ioloop.IOLoop.current().run_sync(async_http_request)