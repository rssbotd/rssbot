# This file is placed in the Public Domain.


"persistence"


import datetime
import json.decoder
import os
import pathlib
import threading


from .cache  import Cache, fntime, search
from .object import Object, fqn, update
from .serial import dump, load


lock = threading.RLock()
j    = os.path.join


class Error(Exception):

    pass


class Workdir:

    name = __file__.rsplit(os.sep, maxsplit=2)[-2]
    wdr = ""


def cdir(path):
    pth = pathlib.Path(path)
    pth.parent.mkdir(parents=True, exist_ok=True)


def fns(clz):
    pth = store(clz)
    for rootdir, dirs, _files in os.walk(pth, topdown=False):
        if dirs:
            for dname in dirs:
                if dname.count('-') == 2:
                    ddd = j(rootdir, dname)
                    for fll in os.listdir(ddd):
                        yield strip(j(ddd, fll))


def getpath(obj):
    return j(store(ident(obj)))


def ident(obj):
    return j(fqn(obj),*str(datetime.datetime.now()).split())


def isdeleted(obj):
    return '__deleted__' in dir(obj) and obj.__deleted__


def last(obj, selector=None):
    if selector is None:
        selector = {}
    result = sorted(locate(fqn(obj), selector), key=lambda x: fntime(x[0]))
    res = ""
    if result:
        inp = result[-1]
        update(obj, inp[-1])
        res = inp[0]
    return res


def locate(clz, selector=None, deleted=False, matching=False):
    skel()
    res = []
    clz = long(clz)
    if selector is None:
        selector = {}
    for pth in fns(clz):
        obj = Cache.get(pth)
        if not obj:
            obj = Object()
            read(obj, store(pth))
            Cache.add(pth, obj)
        if not deleted and isdeleted(obj):
            continue
        if selector and not search(obj, selector, matching):
            continue
        res.append((pth, obj))
    return sorted(res, key=lambda x: fntime(x[0]))


def long(name):
    split = name.split(".")[-1].lower()
    res = name
    for names in types():
        if split == names.split(".")[-1].lower():
            res = names
            break
    return res


def read(obj, path):
    with lock:
        with open(path, "r", encoding="utf-8") as fpt:
            try:
                update(obj, load(fpt))
            except json.decoder.JSONDecodeError as ex:
                raise Error(path) from ex
        Cache.update(path, obj)


def setwd(name, path=""):
    path = path or os.path.expanduser(f"~/.{name}")
    Workdir.wdr = path


def skel():
    pth = pathlib.Path(store())
    pth.mkdir(parents=True, exist_ok=True)
    return str(pth)


def store(pth=""):
    return j(Workdir.wdr, "store", pth)


def strip(pth, nmr=3):
    return j(*pth.split(os.sep)[-nmr:])


def types():
    return os.listdir(store())


def write(obj, path=""):
    with lock:
        if path == "":
            path = getpath(obj)
        cdir(path)
        with open(path, "w", encoding="utf-8") as fpt:
            dump(obj, fpt, indent=4)
        Cache.update(path, obj)
        return path


def __dir__():
    return (
        'Error',
        'Workdir',
        'cdir',
        'fns',
        'getpath',
        'ident',
        'locate',
        'read',
        'setwd',
        'store',
        'strip',
        'write'
    )
