# This file is placed in the Public Domain.
# pylint: disable=C0103,C0115,C0116,C0209,C0301,R0903,W0105,W0201,W0613,E0402


"rest"


import os
import sys
import time


from http.server import HTTPServer, BaseHTTPRequestHandler


from ..default import Default
from ..objects import Object
from ..threads import later, launch


a = os.path.abspath
d = os.path.dirname
p = os.path.join


BASE = p(d(d(__file__)), "html", "")
DEBUG = False


def init():
    try:
        rest = HTTP((Config.hostname, int(Config.port)), HTTPHandler)
    except OSError as ex:
        rest = None
        later(ex)
    if rest is not None:
        rest.start()
    return rest


def html2(txt):
    return """<!doctype html>
<html>
   %s
</html>
""" % txt


class WebError(Exception):

    pass


class Config(Default):

    hostname = "localhost"
    port     = 8000


class HTTP(HTTPServer, Object):

    daemon_thread = True
    allow_reuse_address = True

    def __init__(self, *args, **kwargs):
        HTTPServer.__init__(self, *args, **kwargs)
        Object.__init__(self)
        self.host = args[0]
        self._starttime = time.time()
        self._last = time.time()
        self._status = "start"

    def exit(self):
        time.sleep(0.2)
        self._status = ""
        self.shutdown()

    def start(self):
        launch(self.serve_forever)
        self._status = "ok"

    def request(self):
        self._last = time.time()

    def error(self, _request, _addr):
        exctype, excvalue, _trb = sys.exc_info()
        exc = exctype(excvalue)
        later(exc)


class HTTPHandler(BaseHTTPRequestHandler):

    def setup(self):
        BaseHTTPRequestHandler.setup(self)
        self._size = 0
        self._ip = self.client_address[0]

    def raw(self, data):
        self.wfile.write(data)

    def send(self, txt):
        self.wfile.write(bytes(txt, encoding="utf-8"))
        self.wfile.flush()

    def write_header(self, htype='text/plain', size=None):
        self.send_response(200)
        #self.send_header(
        #                  'Content-type',
        #                  '%s; charset=%s ' % (htype, "utf-8")
        #                 )
        self.send_header('Content-type', '%s;')
        if size is not None:
            self.send_header('Content-length', size)
        self.send_header('Server', "1")
        self.end_headers()

    def log(self, code):
        pass

    def do_GET(self):
        if "favicon" in self.path:
            return
        if DEBUG:
            return
        if self.path == "/":
            self.path = "/index.html"
        path = a(BASE + self.path)
        if not os.path.exists(path):
            self.write_header("text/html")
            self.send_response(404)
            self.end_headers()
            return
        if "_images" in self.path:
            try:
                with open(path, "rb") as file:
                    img = file.read()
                    file.close()
                ext = self.path[-3]
                self.write_header(f"image/{ext}", len(img))
                self.raw(img)
            except (
                    TypeError,
                    FileNotFoundError,
                    IsADirectoryError
                   ) as ex:
                self.send_response(404)
                later(ex)
                self.end_headers()
            return
        try:
            with open(
                      path,
                      "r",
                      encoding="utf-8",
                      errors="ignore"
                     ) as file:
                txt = file.read()
                file.close()
            self.write_header("text/html")
            self.send(html2(txt))
        except (TypeError, FileNotFoundError, IsADirectoryError) as ex:
            self.send_response(404)
            later(ex)
            self.end_headers()
