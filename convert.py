#!/usr/bin/env python
# coding: utf-8

import collections


def convert_unicode(data):
    if isinstance(data, str):
        return data.decode('utf8')
    elif isinstance(data, collections.Mapping):
        return dict(map(convert_unicode, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert_unicode, data))
    else:
        return data
