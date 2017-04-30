# coding: utf-8

import gevent


def pri():
    while True:
        a = 1


gevent.joinall([
    gevent.spawn(pri)
])
