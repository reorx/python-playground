#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2


test_url = 'http://ns223506.ovh.net/rozne/6535bbadbd1d4b524dba1feb2316123a/wallpaper-2253361.jpg'


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

    sys.exit()

    file_size_dl = 0
    block_sz = 8192
    while True:
        _buffer = resp.read(block_sz)
        if not _buffer:
            break

        file_size_dl += len(_buffer)
        f.write(_buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8) * (len(status) + 1)
        #print status,

    f.close()
    print 'Done %s' % file_name


def downloadChunks(url):
    """Helper to download large files
        the only arg is a url
       this file will go to a temp directory
       the file will also be downloaded
       in chunks and print out how much remains
    """

    baseFile = os.path.basename(url)

    #move the file to a more uniq path
    os.umask(0002)
    temp_path = "/tmp/"
    try:
        file = os.path.join(temp_path,baseFile)

        req = urllib2.urlopen(url)
        total_size = int(req.info().getheader('Content-Length').strip())
        downloaded = 0
        CHUNK = 256 * 10240
        with open(file, 'wb') as fp:
            while True:
                chunk = req.read(CHUNK)
                downloaded += len(chunk)
                print math.floor( (downloaded / total_size) * 100 )
                if not chunk: break
                fp.write(chunk)
    except urllib2.HTTPError, e:
        print "HTTP Error:",e.code , url
        return False
    except urllib2.URLError, e:
        print "URL Error:",e.reason , url
        return False

    return file


if __name__ == '__main__':
    file_downloader(test_url)
