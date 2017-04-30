# coding: utf-8

import logging
import gevent
#from gevent.queue import Queue
from gevent.queue import JoinableQueue

logging.basicConfig(level=logging.INFO)


q = JoinableQueue()


def worker():
    while True:
        xx = q.get()
        print 'get', xx


gevent.joinall([
    gevent.spawn(worker)
])
