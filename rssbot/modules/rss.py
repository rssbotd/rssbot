# This file is placed in the Public Domain.
# pylint: disable=C,R,W0105,W0622


"rich site syndicate"


import html
import html.parser
import re
import time
import urllib
import urllib.request
import uuid
import _thread


from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus, urlencode


from ..object  import Object, format, update
from ..persist import Cache, find, fntime, last, ident, write
from ..runtime import Repeater, launch


DEBUG = False


fetchlock  = _thread.allocate_lock()


def init():
    fetcher = Fetcher()
    fetcher.start()
    return fetcher


def spl(txt):
    try:
        result = txt.split(',')
    except (TypeError, ValueError):
        result = txt
    return [x for x in result if x]


class Feed(Object):

    def __init__(self):
        Object.__init__(self)
        self.link = ""


class Rss(Object):

    def __init__(self):
        Object.__init__(self)
        self.display_list = 'title,link,author'
        self.insertid     = None
        self.rss          = ''


class Urls(Object):

    pass


class Fetcher(Object):

    def __init__(self):
        self.dosave = False
        self.seen = Urls()
        self.seenfn = None

    @staticmethod
    def display(obj):
        result = ''
        displaylist = []
        try:
            displaylist = obj.display_list or 'title,link'
        except AttributeError:
            displaylist = 'title,link,author'
        for key in displaylist.split(","):
            if not key:
                continue
            data = getattr(obj, key, None)
            if not data:
                continue
            data = data.replace('\n', ' ')
            data = striphtml(data.rstrip())
            data = unescape(data)
            result += data.rstrip()
            result += ' - '
        return result[:-2].rstrip()

    def fetch(self, feed, silent=False):
        with fetchlock:
            result = []
            seen = getattr(self.seen, feed.rss, [])
            urls = []
            counter = 0
            for obj in reversed(getfeed(feed.rss, feed.display_list)):
                counter += 1
                fed = Feed()
                update(fed, obj)
                update(fed, feed)
                url = urllib.parse.urlparse(fed.link)
                if url.path and not url.path == '/':
                    uurl = f'{url.scheme}://{url.netloc}/{url.path}'
                else:
                    uurl = fed.link
                urls.append(uurl)
                if uurl in seen:
                    continue
                if self.dosave:
                    write(fed, ident(fed))
                result.append(fed)
            setattr(self.seen, feed.rss, urls)
            if not self.seenfn:
                self.seenfn = ident(self.seen)
            write(self.seen, self.seenfn)
        if silent:
            return counter
        txt = ''
        feedname = getattr(feed, 'name', None)
        if feedname:
            txt = f'[{feedname}] '
        for obj in result:
            txt2 = txt + self.display(obj)
            for obj in Cache.typed("IRC"):
                obj.announce(txt2)
        return counter

    def run(self, silent=False):
        thrs = []
        for _fn, feed in find('rss'):
            thrs.append(launch(self.fetch, feed, silent))
        return thrs

    def start(self, repeat=True):
        self.seenfn = last(self.seen)
        if repeat:
            repeater = Repeater(300.0, self.run)
            repeater.start()


class Parser:

    @staticmethod
    def getitem(line, item):
        lne = ''
        index1 = line.find(f'<{item}>')
        if index1 == -1:
            return lne
        index1 += len(item) + 2
        index2 = line.find(f'</{item}>', index1)
        if index2 == -1:
            return lne
        lne = line[index1:index2]
        lne = cdata(lne)
        return lne.strip()

    @staticmethod
    def getitems(text, token):
        index = 0
        result = []
        stop = False
        while not stop:
            index1 = text.find(f'<{token}', index)
            if index1 == -1:
                break
            index1 += len(token) + 2
            index2 = text.find(f'</{token}>', index1)
            if index2 == -1:
                break
            lne = text[index1:index2]
            result.append(lne)
            index = index2
        return result

    @staticmethod
    def parse(txt, toke="item", items='title,link'):
        result = []
        for line in Parser.getitems(txt, toke):
            line = line.strip()
            obj = Object()
            for itm in spl(items):
                val = Parser.getitem(line, itm)
                if val:
                    val = unescape(val.strip())
                    val = val.replace("\n", "")
                    val = striphtml(val)
                    setattr(obj, itm, val)
            result.append(obj)
        return result



def cdata(line):
    if 'CDATA' in line:
        lne = line.replace('![CDATA[', '')
        lne = lne.replace(']]', '')
        lne = lne[1:-1]
        return lne
    return line


def getfeed(url, items):
    result = [Object(), Object()]
    if DEBUG:
        return result
    try:
        rest = geturl(url)
    except (ValueError, HTTPError, URLError):
        return result
    if rest:
        if url.endswith('atom'):
            result = Parser.parse(str(rest.data, 'utf-8'), 'entry', items) or []
        else:
            result = Parser.parse(str(rest.data, 'utf-8'), 'item', items) or []
    return result


def gettinyurl(url):
    postarray = [
        ('submit', 'submit'),
        ('url', url),
    ]
    postdata = urlencode(postarray, quote_via=quote_plus)
    req = urllib.request.Request('http://tinyurl.com/create.php',
                  data=bytes(postdata, 'UTF-8'))
    req.add_header('User-agent', useragent("rss fetcher"))
    with urllib.request.urlopen(req) as htm: # nosec
        for txt in htm.readlines():
            line = txt.decode('UTF-8').strip()
            i = re.search('data-clipboard-text="(.*?)"', line, re.M)
            if i:
                return i.groups()
    return []


def geturl(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return ""
    url = urllib.parse.urlunparse(urllib.parse.urlparse(url))
    req = urllib.request.Request(url)
    req.add_header('User-agent', useragent("rss fetcher"))
    with urllib.request.urlopen(req) as response: # nosec
        response.data = response.read()
        return response


def shortid():
    return str(uuid.uuid4())[:8]


def striphtml(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def unescape(text):
    txt = re.sub(r'\s+', ' ', text)
    return html.unescape(txt)


def useragent(txt):
    return 'Mozilla/5.0 (X11; Linux x86_64) ' + txt
