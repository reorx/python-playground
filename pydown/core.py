#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

get_now_str = lambda: datetime.datetime.now().strftime('%Y:%m:%d %H:%M:%S')


class Pydown(object):
    def __init__(self, engine_name='urllib2', chunk_size=1024 * 500):
        self.engine_name = engine_name
        self.chunk_size = chunk_size

        self.history = []

    def set_engine(self):
        """
        urllib, urllib2, requests, wget
        """
        pass

    def urllib_download(self, url):
        pass

    def urllib2_download(self, url):
        pass

    def requests_download(self, url):
        """
        requires requests lib
        """
        try:
            import requests
        except ImportError:
            pass
        pass

    def wget_download(self, url):
        """
        requires wget command
        """
        pass

    def _write_file(self):
        pass

    def download(self, url):
        url = url
        record = {
            'url': url,
            'start': get_now_str(),
            'end': None
        }

        resp = self.get(url)
        return getattr(self, '%s_get' % self.engine_name)(url)

        self.history.append(self._record)
        pass
