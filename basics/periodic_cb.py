import tornado.ioloop

def task_function():
    print('Do some work.')

if __name__ == "__main__":
    tornado.ioloop.PeriodicCallback(task_function, 1000).start()
    tornado.ioloop.IOLoop.instance().start()
