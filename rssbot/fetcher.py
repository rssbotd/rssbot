# This file is placed in the Public Domain.


"fectch feeds"


import urllib
import urllib.error
import urllib.parse
import urllib.request


from .methods import Method
from .objects import Data
from .utility import Utils


class Fetcher:

    modified = {}

    @classmethod
    def geturl(cls, url, force=False):
        "fetch an url."
        url = urllib.parse.urlunparse(urllib.parse.urlparse(url))
        req = urllib.request.Request(str(url))
        req.add_header("User-Agent", Utils.useragent("RSS Fetcher"))
        since = cls.modified.get(url, "")
        if since:
            req.add_header('If-Modified-Since', since)
        response = Data()
        response.reason = ""
        try:
            Method.update(response, cls.request(req))
        except Exception as ex:
            response.data = b""
            try:
                response.reason = ex.reason
            except AttributeError:
                response.reason = str(ex)
            try:
                response.status = ex.status
            except AttributeError:
                response.status = 0
        return response

    @classmethod
    def request(cls, req):
        with urllib.request.urlopen(req, timeout=4) as response:  # nosec
            modi = response.headers.get('Last-Modified', "")
            if modi:
                cls.modified[req.get_full_url()] = modi
            response.data = response.read()
            response.error = ""
            return response


def __dir__():
    return (
        'Fetcher',
    )
