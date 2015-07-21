#!/usr/bin/env python

import time
from tornado.ioloop import IOLoop, PeriodicCallback

def task_function():
    print 'Do some work.'

if __name__ == "__main__":
    PeriodicCallback(task_function, 1000).start()
    IOLoop.instance().start()
