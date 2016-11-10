#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

test_url = 'http://download.thinkbroadband.com/10MB.zip'


def file_downloader(url, file_name=None):
    # get file_name
    if not file_name:
        file_name = url.split('/')[-1]

    resp = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = resp.info()
    print 'meta: ', meta
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    f.write(resp.read())

    f.close()
    print 'Done %s' % file_name


if __name__ == '__main__':
    file_downloader(test_url)
