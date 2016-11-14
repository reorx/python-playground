# coding: utf-8

import short_id


def test_simple():
    for i in [
        1, 10, 100, 1000,
        1e5, 1e6, 1e9, 1e10,
        1e11, 1e15, 1e17,
        #1e18, int(1e18) - 1, int(1e18) - 2,
    ]:
        print '{}: {}'.format(i, short_id.encode_url(int(i)))
