#!/usr/bin/env python
#
# Simplify asynchronous code

import time
from tornado.ioloop import IOLoop
from tornado import gen
 
def task_function(callback):
    print 'Do some work and call the callback.'
    callback(123)
  
@gen.engine
def func():
    print 'Start and call the task_function, then print result and stop the ioloop.'
    result = yield gen.Task(task_function)
    print 'The result is', result
    IOLoop.instance().stop()
 
if __name__ == "__main__":
    IOLoop.instance().add_callback(func)
    IOLoop.instance().add_callback(func)
    IOLoop.instance().add_callback(func)
    IOLoop.instance().start()
