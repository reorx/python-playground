#!/usr/bin/env python
# -*- coding: utf-8 -*-

A = 1


def foo():
    print 'A', A
    #A = A + 1
    a = 1

    def bar():
        #a = a + 1
        print 'bar a', a

    bar()


if __name__ == '__main__':
    foo()
