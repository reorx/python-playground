import json
from typing import Optional, Tuple, Union
from urllib import request, parse
from http.client import HTTPResponse, IncompleteRead


# overload is too complicated
#@overload
#def http_request(method, url, params=None, headers=None, data: Optional[Union[dict, list, bytes]] = None, return_bytes: Literal[True] = True, timeout=None, logger=None) -> Tuple[HTTPResponse, bytes]: ...
#
#@overload
#def http_request(method, url, params=None, headers=None, data: Optional[Union[dict, list, bytes]] = None, return_bytes: Literal[False] = False, timeout=None, logger=None) -> Tuple[HTTPResponse, str]: ...


def http_request(method, url, params=None, headers=None, data: Optional[Union[dict, list, bytes]] = None, timeout=None, logger=None) -> Tuple[HTTPResponse, bytes]:
    if params:
        url = f'{url}?{parse.urlencode(params)}'
    if not headers:
        headers = {}
    if data and isinstance(data, (dict, list)):
        data = json.dumps(data, ensure_ascii=False).encode()
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json; charset=utf-8'
    if logger:
        logger.info(f'request: {method} {url}')
    req = request.Request(url, method=method, headers=headers, data=data)
    res = request.urlopen(req, timeout=timeout)  # raises: (HTTPException, urllib.error.URLError)
    try:
        body_b: bytes = res.read()
    except IncompleteRead as e:
        body_b: bytes = e.partial
    if logger:
        logger.debug(f'response: {res.status}, {body_b}')
    return res, body_b


class RequestError(Exception):
    def __init__(self, status, body) -> None:
        self.status = status
        self.body = body

    def __str__(self):
        return f'{self.__class__.__name__}: {self.status}, {self.body}'
