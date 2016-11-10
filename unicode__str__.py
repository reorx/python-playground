#!/usr/bin/env python
# coding: utf-8

import traceback
import logging


A_UNICODE = u'尤尼扣得'
A_STR = '字符串'


print "\n# Case 1. u'sth %s' % '字符串'"

try:
    x = u'sth %s' % A_STR
    print type(x)
    print x
except UnicodeDecodeError:
    traceback.print_exc()

print "\n# Case 2. 'sth %s' % u'尤尼扣得'"

x = 'sth %s' % u'尤尼扣得'
print type(x)
print x

print "\n# Case 3. '字符串 %s' % u'尤尼扣得'"

try:
    x = '字符串 %s' % u'尤尼扣得'
    print type(x)
    print x
except UnicodeDecodeError:
    traceback.print_exc()

print "\n# Case 4. logging.info(Exception(A_STR))"

logging.basicConfig(level=logging.INFO)
logging.info(Exception(A_STR))

print "\n# Case 5. logging.info('str %s', Exception(A_STR))"

logging.info('sth %s', Exception(A_STR))

print "\n# Case 6. logging.info('str %s', Exception(A_UNICODE))"

try:
    logging.info('sth %s', Exception(A_UNICODE))
except UnicodeEncodeError:
    traceback.print_exc()

print "\n# Case 7. logging.info(u'unicode %s', Exception(A_STR))"
try:
    logging.info(u'unicode %s', Exception(A_STR))
except UnicodeDecodeError:
    traceback.print_exc()

print "\n# Case 8. logging.info(u'尤尼扣得 %s', Exception(A_UNICODE))"
logging.info(u'尤尼扣得 %s', Exception(A_UNICODE))
