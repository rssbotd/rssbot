# This file is placed in the Public Domain.


"persistence"


import datetime
import os
import json
import pathlib
import threading
import time
import typing


from .object import Object, dumps, fqn, loads, search, update


p    = os.path.join
lock = threading.RLock()


class DecodeError(Exception):

    pass


class Workdir:

    name = __file__.rsplit(os.sep, maxsplit=2)[-2]
    wdr  = ""


class Cache:

    objs = {}

    @staticmethod
    def add(path, obj) -> None:
        Cache.objs[path] = obj

    @staticmethod
    def get(path) -> typing.Any:
        return Cache.objs.get(path, None)

    @staticmethod
    def typed(matcher) -> [typing.Any]:
        for key in Cache.objs:
            if matcher not in key:
                continue
            yield Cache.objs.get(key)


"paths"


def long(name) -> str:
    split = name.split(".")[-1].lower()
    res = name
    for names in types():
        if split == names.split(".")[-1].lower():
            res = names
            break
    return res


def pidname(name) -> str:
    return p(Workdir.wdr, f"{name}.pid")


def store(pth="") -> str:
    return p(Workdir.wdr, "store", pth)


def strip(pth, nmr=2) -> str:
    return os.sep.join(pth.split(os.sep)[-nmr:])


def types() -> [str]:
    return os.listdir(store())


"find"


def fns(clz) -> [str]:
    pth = store(clz)
    for rootdir, dirs, _files in os.walk(pth, topdown=False):
        if dirs:
            for dname in sorted(dirs):
                if dname.count('-') == 2:
                     ddd = p(rootdir, dname)
                     for fll in os.listdir(ddd):
                         yield p(ddd, fll)


def fntime(daystr) -> int:
    datestr = ' '.join(daystr.split(os.sep)[-2:])
    datestr = datestr.replace("_", " ")
    if '.' in datestr:
        datestr, rest = datestr.rsplit('.', 1)
    else:
        rest = ''
    timed = time.mktime(time.strptime(datestr, '%Y-%m-%d %H:%M:%S'))
    if rest:
        timed += float('.' + rest)
    return timed


def find(clz, selector=None, deleted=False, matching=False) -> [Object]:
    res = []
    skel()
    res = []
    clz = long(clz)
    for pth in fns(clz):
        obj = Cache.get(pth)
        if not obj:
            obj = Object()
            read(obj, pth)
            Cache.add(pth, obj)
        if not deleted and '__deleted__' in dir(obj) and obj.__deleted__:
            continue
        if selector and not search(obj, selector, matching):
            continue
        res.append((pth, obj))
    return sorted(res, key=lambda x: fntime(x[0]))


"utilities"


def cdir(pth) -> None:
    path = pathlib.Path(pth)
    path.parent.mkdir(parents=True, exist_ok=True)


def elapsed(seconds, short=True) -> str:
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


def skel() -> str:
    path = pathlib.Path(store())
    path.mkdir(parents=True, exist_ok=True)
    return path


def spl(txt) -> str:
    """ iterate over comma seperated string. """
    try:
        result = txt.split(',')
    except (TypeError, ValueError):
        result = txt
    return [x for x in result if x]


"methods"


def ident(obj) -> str:
    return p(fqn(obj),*str(datetime.datetime.now()).split())


def last(obj, selector=None) -> Object:
    if selector is None:
        selector = {}
    result = sorted(
                    find(fqn(obj), selector),
                    key=lambda x: fntime(x[0])
                   )
    res = None
    if result:
        inp = result[-1]
        update(obj, inp[-1])
        res = inp[0]
    return res



def read(obj, pth):
    with open(pth, 'r', encoding='utf-8') as ofile:
        try:
            obj2 = loads(ofile.read())
            update(obj, obj2)
        except json.decoder.JSONDecodeError as ex:
            raise DecodeError(pth) from ex
    return pth


def write(obj, pth):
    with lock:
        cdir(pth)
        txt = dumps(obj, indent=4)
        Cache.objs[pth] = obj
        with open(pth, 'w', encoding='utf-8') as ofile:
            ofile.write(txt)
    return pth


"interface"


def __dir__():
    return (
        'DecodeError',
        'Workdir',
        'cdir',
        'fns',
        'fntime',
        'find',
        'last',
        'pidname',
        'read',
        'skel',
        'types',
        'write'
    )
