# This file is placed in the Public Domain.


"fectch feeds"


import html
import re
import urllib
import urllib.error
import urllib.parse
import urllib.request


from .methods import Method
from .objects import Data


class Fetcher:

    modified = {}

    @classmethod
    def geturl(cls, url, force=False):
        "fetch an url."
        url = urllib.parse.urlunparse(urllib.parse.urlparse(url))
        req = urllib.request.Request(str(url))
        req.add_header("User-Agent", cls.useragent("RSS Fetcher"))
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

    @staticmethod
    def striphtml(text):
        "strip html."
        clean = re.compile("<.*?>")
        return re.sub(clean, "", text)

    @staticmethod
    def unescape(text):
        "unescape html."
        txt = re.sub(r"\s+", " ", text)
        return html.unescape(txt)

    @staticmethod
    def unquote(url):
        "unquote an url."
        return urllib.parse.unquote(url, errors='ignore')

    @staticmethod
    def useragent(txt):
        "produce useragent string."
        return "Mozilla/5.0 (X11; Linux x86_64) " + txt


def __dir__():
    return (
        'Fetcher',
    )
