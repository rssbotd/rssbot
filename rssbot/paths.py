# This file is placed in the Public Domain.


"workdir"


import os
import pathlib


class Workdir:

    name = __file__.rsplit(os.sep, maxsplit=2)[-2]
    wdr = ""


def long(name):
    split = name.split(".")[-1].lower()
    res = name
    for names in types():
        if split == names.split(".")[-1].lower():
            res = names
            break
    return res


def moddir():
    return os.path.join(Workdir.wdr, "mods")


def pidname(name):
    return os.path.join(Workdir.wdr, f"{name}.pid")


def skel():
    pth = pathlib.Path(store())
    pth.mkdir(parents=True, exist_ok=True)
    pth = pathlib.Path(moddir())
    pth.mkdir(parents=True, exist_ok=True)
    return str(pth)


def store(pth=""):
    return os.path.join(Workdir.wdr, "store", pth)


def strip(pth, nmr=2):
    return os.path.join(pth.split(os.sep)[-nmr:])


def types():
    return os.listdir(store())


def wdr(pth):
    return os.path.join(Workdir.wdr, pth)


def __dir__():
    return (
        'Workdir',
        'long',
        'moddir',
        'pidname',
        'skel',
        'store',
        'strip',
        'wdr'
    )
