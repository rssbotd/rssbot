# This file is placed in the Public Domain.
# pylint: disable=C,R,W0105,W0718


"command"


import inspect
import os
import sys
import time
import _thread


from .modules import face
from .object  import Obj, edit, format, keys
from .persist import Workdir, find, fntime, last, write
from .runtime import Client, Event, errors, later, launch


NAME        = __file__.rsplit(os.sep, maxsplit=2)[-2]
Workdir.wdr = os.path.expanduser(f"~/.{NAME}")


class Config(Obj):

    pass


Cfg  = Config()


class Commands:

    cmds = {}

    @staticmethod
    def add(func):
        Commands.cmds[func.__name__] = func

    @staticmethod
    def scan(mod):
        for key, cmdz in inspect.getmembers(mod, inspect.isfunction):
            if key.startswith("cb"):
                continue
            if 'event' in cmdz.__code__.co_varnames:
                Commands.add(cmdz)


def command(bot, evt):
    parse(evt, evt.txt)
    if "ident" in dir(bot):
        evt.orig = bot.ident
    func = Commands.cmds.get(evt.cmd, None)
    if func:
        try:
            func(evt)
            bot.display(evt)
        except Exception as ex:
            later(ex)
    evt.ready()


class CLI(Client):

    def __init__(self):
        Client.__init__(self)
        self.register("command", command)

    def raw(self, txt):
        print(txt)


"utilities"


def laps(seconds, short=True) -> str:
    txt = ""
    nsec = float(seconds)
    if nsec < 1:
        return f"{nsec:.2f}s"
    yea = 365*24*60*60
    week = 7*24*60*60
    nday = 24*60*60
    hour = 60*60
    minute = 60
    yeas = int(nsec/yea)
    nsec -= yeas*yea
    weeks = int(nsec/week)
    nsec -= weeks*week
    nrdays = int(nsec/nday)
    nsec -= nrdays*nday
    hours = int(nsec/hour)
    nsec -= hours*hour
    minutes = int(nsec/minute)
    nsec -= int(minute*minutes)
    sec = int(nsec)
    if yeas:
        txt += f"{yeas}y"
    if weeks:
        nrdays += weeks * 7
    if nrdays:
        txt += f"{nrdays}d"
    if short and txt:
        return txt.strip()
    if hours:
        txt += f"{hours}h"
    if minutes:
        txt += f"{minutes}m"
    if sec:
        txt += f"{sec}s"
    txt = txt.strip()
    return txt


def parse(obj, txt=None):
    if txt is None:
        txt = ""
    args = []
    obj.args    = []
    obj.cmd     = ""
    obj.gets    = Obj()
    obj.hasmods = False
    obj.index   = None
    obj.mod     = ""
    obj.opts    = ""
    obj.result  = []
    obj.sets    = Obj()
    obj.txt     = txt or ""
    obj.otxt    = obj.txt
    _nr = -1
    for spli in obj.otxt.split():
        if spli.startswith("-"):
            try:
                obj.index = int(spli[1:])
            except ValueError:
                obj.opts += spli[1:]
            continue
        if "==" in spli:
            key, value = spli.split("==", maxsplit=1)
            val = getattr(obj.gets, key, None)
            if val:
                value = val + "," + value
                setattr(obj.gets, key, value)
            continue
        if "=" in spli:
            key, value = spli.split("=", maxsplit=1)
            if key == "mod":
                obj.hasmods = True
                if obj.mod:
                    obj.mod += f",{value}"
                else:
                    obj.mod = value
                continue
            setattr(obj.sets, key, value)
            continue
        _nr += 1
        if _nr == 0:
            obj.cmd = spli
            continue
        args.append(spli)
    if args:
        obj.args = args
        obj.txt  = obj.cmd or ""
        obj.rest = " ".join(obj.args)
        obj.txt  = obj.cmd + " " + obj.rest
    else:
        obj.txt = obj.cmd or ""
    return obj


def spl(txt):
    try:
        result = txt.split(',')
    except (TypeError, ValueError):
        result = txt
    return [x for x in result if x]


"commands"


def cfg(event):
    from .modules.irc import Config
    config = Config()
    last(config)
    if not event.sets:
        event.reply(
                    format(
                        config,
                        keys(config),
                        skip='control,password,realname,sleep,username'.split(",")
                       )
                   )
    else:
        edit(config, event.sets)
        write(config)
        event.reply('ok')


def cmd(event):
    event.reply(",".join(sorted(keys(Commands.cmds))))


def dpl(event):
    if len(event.args) < 2:
        event.reply('dpl <stringinurl> <item1,item2>')
        return
    setter = {'display_list': event.args[1]}
    for fnm, feed in find("rss", {'rss': event.args[0]}):
        if feed:
            update(feed, setter)
            write(feed, fnm)
    event.reply('ok')


def nme(event):
    if len(event.args) != 2:
        event.reply('nme <stringinurl> <name>')
        return
    selector = {'rss': event.args[0]}
    for fnm, feed in find("rss", selector):
        if feed:
            feed.name = event.args[1]
            write(feed, fnm)
    event.reply('ok')


def pwd(event):
    if len(event.args) != 2:
        event.reply('pwd <nick> <password>')
        return
    arg1 = event.args[0]
    arg2 = event.args[1]
    txt = f'\x00{arg1}\x00{arg2}'
    enc = txt.encode('ascii')
    base = base64.b64encode(enc)
    dcd = base.decode('ascii')
    event.reply(dcd)


def rem(event):
    if len(event.args) != 1:
        event.reply('rem <stringinurl>')
        return
    for fnm, feed in find("rss"):
        if event.args[0] not in feed.rss:
            continue
        if feed:
            feed.__deleted__ = True
            write(feed, fnm)
    event.reply('ok')


def res(event):
    if len(event.args) != 1:
        event.reply('res <stringinurl>')
        return
    for fnm, feed in find("rss", deleted=True):
        if event.args[0] not in feed.rss:
            continue
        if feed:
            feed.__deleted__ = False
            write(feed, fnm)
    event.reply('ok')


def rss(event):
    from .modules.rss import Rss
    if not event.rest:
        nrs = 0
        for fnm, feed in find('rss'):
            nrs += 1
            elp = laps(time.time()-fntime(fnm))
            txt = format(feed)
            event.reply(f'{nrs} {txt} {elp}')
        if not nrs:
            event.reply('no rss feed found.')
        return
    url = event.args[0]
    if 'http' not in url:
        event.reply('i need an url')
        return
    for fnm, result in find("rss", {'rss': url}):
        if result:
            return
    feed = Rss()
    feed.rss = event.args[0]
    write(feed, ident(feed))
    event.reply('ok')


def srv(event):
    import getpass
    name  = getpass.getuser()
    event.reply(TXT % (NAME.upper(), name, name, name, NAME))


def syn(event):
    from .modules.rss import Fetcher
    fetcher = Fetcher()
    fetcher.start(False)
    thrs = fetcher.run(True)
    nrs = 0
    for thr in thrs:
        thr.join()
        nrs += 1
    event.reply(f"{nrs} feeds synced")


"runtime"


def wrap(func):
    try:
        func()
    except (KeyboardInterrupt, EOFError):
        pass
    except Exception as ex:
        later(ex)


def wrapped():
    wrap(main)
    for line in errors():
        print(line)


def main():
    parse(Cfg, " ".join(sys.argv[1:]))
    mod = sys.modules.get("__main__")
    Commands.scan(mod)
    evt = Event()
    evt.type = "command"
    evt.txt = Cfg.otxt
    csl = CLI()
    command(csl, evt)
    evt.wait()


TXT = """[Unit]
Description=%s
After=network-online.target

[Service]
Type=simple
User=%s
Group=%s
ExecStart=/home/%s/.local/bin/%ss

[Install]
WantedBy=multi-user.target"""


if __name__ == "__main__":
    wrapped()
