# This file is placed in the Public Domain.


"rich site syndicate"


import errno
import http.client
import logging
import os
import queue
import re
import threading
import urllib
import urllib.parse
import urllib.request
import _thread


from urllib.error import HTTPError
from urllib.parse import quote_plus, urlencode


from rssbot.defines import Clients, Disk, Format, JSONL, Locate, Logging, Main
from rssbot.defines import Method, Object, Repeater, Thread, Utils, Watcher
from rssbot.defines import Workdir


j = os.path.join


def init():
    "initialize rss module."
    Run.init()
    nrs = Locate.count("rss")
    txt = f"{nrs} feeds index {Run.state.index}"
    if nrs == 1:
        txt = txt[:-1]
    logging.warning(txt)


def shutdown():
    "shutdown rss module."
    Run.stop()


class Config(Object):

    index = 0
    polltime = 300


class Feed(Object):

    link = ""


class Modified(Object):

    pass


class Urls(Object):

    pass


class Rss(Object):

    def __init__(self):
        super().__init__()
        self.display_list = "title,link,author"
        self.insertid = None
        self.name = ""
        self.rss = ""


class State(Object):

    def __init__(self):
        super().__init__(self)
        self.configfn = ""
        self.index = 0
        self.modifiedfn = ""
        self.seenfn = ""


class Locks:

    fetchlock = _thread.allocate_lock()
    importlock = _thread.allocate_lock()


class Runner:

    def __init__(self):
        self.dosave = True
        self.queue = queue.Queue()
        self.running = threading.Event()
        self.todo = queue.Queue()

    def loop(self):
        "loop to handle fetch jobs."
        while self.running.is_set():
            job = self.queue.get()
            if job is None:
                break
            self.fetch(*job)

    def fetch(self, fnm, feed, silent=False):
        "fetch a feed."
        counter = 0
        with Locks.fetchlock:
            result = []
            see = getattr(Run.seen, feed.rss, [])
            urls = []
            for obj in Helpers.getfeed(fnm, feed, feed.display_list):
                if obj is None:
                    continue
                if Method.isempty(obj):
                    continue
                counter += 1
                fed = Feed()
                Method.update(fed, obj)
                Method.update(fed, feed)
                url = urllib.parse.urlparse(fed.link)
                if url.path and not url.path == "/":
                    uurl = f"{url.scheme}://{url.netloc}/{url.path}"
                else:
                    uurl = fed.link
                urls.append(uurl)
                if uurl in see:
                    continue
                fed.name = feed.name
                result.append(fed)
                if self.dosave:
                    Run.logger.debug(JSONL.logtxt(fed))
            if urls:
                setattr(Run.seen, feed.rss, urls)
            if silent:
                return counter
            if not Run.state.seenfn:
                Run.state.seenfn = Disk.ident(Run.seen)
            Disk.write(Run.seen, Run.state.seenfn)
        return counter

    def put(self, args):
        "put jobs on queue."
        self.queue.put(args)

    def start(self, daemon=True):
        "start runner."
        self.running.set()
        Thread.launch(self.loop, daemon=daemon)

    def stop(self):
        "stop runner."
        self.running.clear()
        self.queue.put(None)


class Runners:

    runners = []
    lock = threading.RLock()
    nrcpu = 1
    nrlast = 0

    @classmethod
    def add(cls, client):
        "add a runner."
        cls.runners.append(client)

    @classmethod
    def init(cls, nrcpu, clazz):
        "initialize a runner."
        cls.nrcpu = nrcpu
        for _x in range(cls.nrcpu):
            clt = clazz()
            clt.start()
            Runners.add(clt)

    @classmethod
    def put(cls, *args):
        "push job to a runner."
        if not cls.runners:
            cls.init(Runners.nrcpu, Runner)
        with cls.lock:
            if cls.nrlast >= cls.nrcpu-1:
                cls.nrlast = 0
            clt = cls.runners[cls.nrlast]
            clt.put(*args)
            cls.nrlast += 1


class Fetcher:

    def __init__(self):
        self.dosave = False
        self.stopped = threading.Event()
        self.todo = queue.Queue()

    def run(self, silent=False):
        "do a fetch run of all feeds."
        nrs = 0
        for fnm, feed in Locate.find(Method.fqn(Rss)):
            Runners.put((fnm, feed, silent))
            nrs += 1
        return nrs

    def start(self, repeat=True):
        "start rss fetcher."
        Disk.read(Config, "rss", "config")
        Run.state.seenfn = Locate.last(Run.seen) or Disk.ident(Run.seen)
        oid = Disk.ident(Run.modified)
        Run.state.modifiedfn = Locate.last(Run.modified) or oid
        if repeat:
            Repeater.add(Config.polltime, self.run)

    def stop(self):
        "sto prss fetcher."
        logging.debug("stopped fetcher")
        if Run.modified:
            Disk.write(Run.modified, Run.state.modifiedfn)
        self.stopped.set()


class RSS:

    @classmethod
    def getitem(cls, line, item):
        "return item from line."
        lne = ""
        index1 = line.find(f"<{item}>")
        if index1 == -1:
            return lne
        index1 += len(item) + 2
        index2 = line.find(f"</{item}>", index1)
        if index2 == -1:
            return lne
        return Utils.cdata(line[index1:index2]).strip()

    @classmethod
    def getitems(cls, text, token, nrs=None):
        "get items from text."
        index = 0
        end = len(text)
        stop = False
        nrx = -1
        while not stop:
            nrx += 1
            if nrs and nrx >= nrs:
                break
            index1 = text.rfind(f"<{token}", index, end)
            if index1 == -1:
                break
            end = index1
            index1 += len(token) + 2
            index2 = text.rfind(f"</{token}>", index1)
            if index2 == -1:
                break
            yield text[index1:index2]

    @classmethod
    def parse(cls, txt, toke="item", items="title,link"):
        "parse feed."
        for line in cls.getitems(txt, toke):
            line = line.strip()
            obj = {}
            for itm in Utils.spl(items):
                val = cls.getitem(line, itm)
                if val:
                    escaped = Utils.unescape(val.strip())
                    obj[itm] = Utils.striphtml(escaped).replace("\n", "")
            yield obj


class Run:

    buffer = []
    fetcher = Fetcher()
    logger = logging.getLogger("rss")
    modified = Modified()
    seen = Urls()
    state = State()
    statefn = ""
    watcher = Watcher()

    @classmethod
    def callback(cls, file):
        if os.fstat(file.fileno()).st_size < cls.state.index:
            cls.state.index = 0
        file.seek(cls.state.index, 0)
        for line in file.readlines():
            if not line:
                continue
            obj = Feed()
            Method.construct(obj, JSONL.loads(line.strip()))
            Clients.announce(cls.display(obj))
        cls.state.index = file.tell()
        Disk.write(cls.state, cls.statefn)
        
    @classmethod
    def display(cls, obj, name=None):
        "display feed."
        displaylist = ""
        if name in obj:
            result = f"[{obj.name}] "
        else:
            result = ""
        try:
            displaylist = obj.display_list or "title,link"
        except AttributeError:
            displaylist = "title,link,author"
        for key in displaylist.split(","):
            if not key:
                continue
            data = getattr(obj, key, None)
            if not data:
                continue
            stripped = Utils.striphtml(data.replace("\n", " ").rstrip())
            result += Utils.unescape(stripped)
            result += " - "
        return result[:-2].rstrip()

    @classmethod
    def enablelog(cls, path):
        "enabke module logger."
        formatter = Format(Logging.formats, Logging.datefmt)
        filehandler = logging.handlers.TimedRotatingFileHandler(path, 'midnight')
        filehandler.setFormatter(formatter)
        if cls.logger.handlers:
            for handler in cls.logger.handlers:
                cls.logger.removeHandler(handler)
        cls.logger.addHandler(filehandler)
        cls.logger.propagate = False
        cls.logger.setLevel("DEBUG")

    @classmethod
    def init(cls):
        "initialise module."
        path = j(Workdir.logdir("rss"), 'rss.log')
        if not os.path.exists(path):
            Utils.cdir(path)
        cls.enablelog(path)
        Watcher.add(path, cls.callback)
        cls.statefn = Locate.last(cls.state)
        cls.fetcher.start()
        cls.watcher.start()
        Runners.init(1, Runner)
        
    @classmethod
    def stop(cls):
        "shutdown."
        cls.fetcher.stop()
        cls.watcher.stop()


class Helpers:

    @staticmethod
    def getfeed(fnm, feed, items):
        "fetch a feed."
        result = [None,]
        try:
            response = Helpers.geturl(feed.rss)
            if not response or not response.data:
                return result
            if "link" not in items:
                items += ",link"
            if feed.rss.endswith("atom"):
                yield from RSS.parse(str(response.data, "utf-8", errors='ignore'),
                                     "entry",
                                     items) or []
            else:
                yield from RSS.parse(str(response.data, "utf-8", errors='ignore'),
                                     "item",
                                     items) or []
            if "error" in feed and feed.error:
                feed.error = ""
                Disk.write(feed, fnm)
        except TimeoutError:
            return result
        except (
                urllib.error.URLError,
                http.client.HTTPException,
                ValueError,
                HTTPError,
                UnicodeDecodeError,
                ConnectionResetError
        ) as ex:
            if '304' in str(ex):
                return result
            feed.error = str(ex)
            logging.debug("%s %s", feed.rss, feed.error)
        except OSError as ex:
            if ex.errno == errno.EBADFD:
                return result
        return result

    @staticmethod
    def gettinyurl(url):
        "query tinyurl for a link."
        postarray = [
            ("submit", "submit"),
            ("url", url),
        ]
        postdata = urlencode(postarray, quote_via=quote_plus)
        req = urllib.request.Request(
            "http://tinyurl.com/create.php", data=bytes(postdata, "UTF-8")
        )
        req.add_header("User-agent", Utils.useragent("rss fetcher"))
        with urllib.request.urlopen(req) as htm:  # nosec
            for txt in htm.readlines():
                line = txt.decode("UTF-8").strip()
                ii = re.search('data-clipboard-text="(.*?)"', line, re.M)
                if ii:
                    return ii.groups()
        return []

    @staticmethod
    def geturl(url, force=False):
        "fetch an url."
        if Main.debug:
            return
        url = urllib.parse.urlunparse(urllib.parse.urlparse(url))
        req = urllib.request.Request(str(url))
        req.add_header("User-Agent", Utils.useragent("RSS Fetcher"))
        if not force:
            since = getattr(Run.modified, url, "")
            if since:
                req.add_header('If-Modified-Since', since)
        logging.debug("fetching %s %s", url, req.headers)
        with urllib.request.urlopen(req, timeout=10.0) as response:  # nosec
            modi = response.headers.get('Last-Modified', "")
            if modi:
                setattr(Run.modified, url, modi)
            response.data = response.read()
            return response


def atr(event):
    "show attributes of a feed."
    if not event.rest:
        event.iface("<stringinurl>")
        return
    for _fnm, obj in Locate.find(Method.fqn(Rss), {'rss': event.rest}):
        request = None
        try:
            request = Helpers.geturl(obj.rss, True)
        except Exception as ex:
            event.reply(str(ex))
            return
        if not request:
            continue
        if obj.rss.endswith('atom'):
            result = list(RSS.getitems(
                                       str(request.data, 'utf-8', errors='ignore'),
                                       'entry',
                                       1))
        else:
            result = list(RSS.getitems(str(request.data, 'utf-8', errors='ignore'),
                                       'item',
                                       1))
        resulting = []
        for x in re.findall('<.*?>', result[0]):
            if x[1] == '/' and len(x) > 4:
                resulting.append(x[2:-1])
        event.reply(','.join(resulting))


def dpl(event):
    "set feed items to display."
    if len(event.args) < 2:
        event.iface("<stringinurl> <item1,item2>")
        return
    setter = {"display_list": event.args[1]}
    for fnm, feed in Locate.find(Method.fqn(Rss), {"rss": event.args[0]}):
        if feed:
            Method.update(feed, setter)
            Disk.write(feed, fnm)
    event.ok()


def nme(event):
    "set name of a feed."
    if len(event.args) == 1:
        name = ""
    elif len(event.args) == 2:
        name = event.args[1]
    else:
        event.iface("<stringinurl> <name>")
        return
    selector = {"rss": event.args[0]}
    for fnm, fed in Locate.find(
                                Method.fqn(Rss),
                                selector
                               ):
        feed = Rss()
        Method.update(feed, fed)
        if feed:
            feed.name = name
            Disk.write(feed, fnm)
    event.ok()


def rem(event):
    "remove a feed."
    if len(event.args) != 1:
        event.iface("<stringinurl>")
        return
    for fnm, fed in Locate.find(Method.fqn(Rss)):
        feed = Rss()
        Method.update(feed, fed)
        if event.args[0] not in feed.rss:
            continue
        if feed:
            feed.__deleted__ = True
            Disk.write(feed, fnm)
            event.ok()
            break


def res(event):
    "restore a feed."
    if len(event.args) != 1:
        event.iface("<stringinurl>")
        return
    nrs = 0
    for fnm, fed in Locate.find(
                                Method.fqn(Rss),
                                removed=True
                               ):
        feed = Rss()
        Method.update(feed, fed)
        if event.args[0] not in feed.rss:
            continue
        nrs += 1
        feed.__deleted__ = False
        Disk.write(feed, fnm)
    event.reply(f"{nrs} feeds restored.")


def rss(event):
    "add a feed."
    if not event.rest:
        event.iface("<url>")
        return
    url = event.args[0]
    if "http://" not in url and "https://" not in url:
        event.reply("i need an url")
        return
    for fnm, result in Locate.find(
                                   Method.fqn(Rss),
                                   {"rss": url}
                                  ):
        if result:
            event.reply(f"{url} is known")
            return
    feed = Rss()
    feed.rss = event.args[0]
    Disk.write(feed)
    event.ok()


def syn(event):
    "synchronize a feed."
    if Main.debug:
        return
    fetcher = Fetcher()
    fetcher.start(False)
    nrs = fetcher.run(True)
    event.reply(f"{nrs} feeds synced")
