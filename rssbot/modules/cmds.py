# This file is placed in the Public Domain.
# pylint: disable=C


"commands"


import base64
import getpass
import os
import time


from ..object  import edit, format, keys, update
from ..persist import find, fntime, ident, laps, last, shortid, write
from ..runtime import Commands


from .irc import Config
from .opm import TEMPLATE, OPMLParser, importlock, skipped
from .rss import Fetcher, Rss


def cfg(event):
    config = Config()
    path = last(config)
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
        write(config, path)
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


def exp(event):
    event.reply(TEMPLATE)
    nrs = 0
    for _fn, ooo in find("rss"):
        nrs += 1
        obj = Rss()
        update(obj, ooo)
        name = f"url{nrs}"
        txt = f'<outline name="{name}" display_list="{obj.display_list}" xmlUrl="{obj.rss}"/>'
        event.reply(" "*12 + txt)
    event.reply(" "*8 + "</outline>")
    event.reply("    <body>")
    event.reply("</opml>")


def imp(event):
    if not event.args:
        event.reply("imp <filename>")
        return
    fnm = event.args[0]
    if not os.path.exists(fnm):
        event.reply(f"no {fnm} file found.")
        return
    with open(fnm, "r", encoding="utf-8") as file:
        txt = file.read()
    prs = OPMLParser()
    nrs = 0
    nrskip = 0
    insertid = shortid()
    with importlock:
        for obj in prs.parse(txt, 'outline', "name,display_list,xmlUrl"):
            url = obj.xmlUrl
            if url in skipped:
                continue
            if not url.startswith("http"):
                continue
            has = list(find("rss", {'rss': url}, matching=True))
            if has:
                skipped.append(url)
                nrskip += 1
                continue
            feed = Rss()
            update(feed, obj)
            feed.rss = obj.xmlUrl
            feed.insertid = insertid
            write(feed, ident(feed))
            nrs += 1
    if nrskip:
        event.reply(f"skipped {nrskip} urls.")
    if nrs:
        event.reply(f"added {nrs} urls.")


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
    name  = getpass.getuser()
    event.reply(TXT % ("RSSBOT", name, name, name, "rssbot"))


def syn(event):
    fetcher = Fetcher()
    fetcher.start(False)
    thrs = fetcher.run(True)
    nrs = 0
    for thr in thrs:
        thr.join()
        nrs += 1
    event.reply(f"{nrs} feeds synced")


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
