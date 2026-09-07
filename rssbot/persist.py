# This file is placed in the Public Domain.


"disk"


import datetime
import os
import threading


from .caching import Cache
from .encoder import JSON
from .methods import Method
from .objects import Data
from .utility import Utils
from .workdir import Workdir


class NoDisk(Exception):

    "disk is disabled."


class DecodeError(Exception):

    "could not parse input."


class Disk:

    disable = False
    lock = threading.RLock()

    @classmethod
    def cached(cls, path, base="store"):
        pth = os.path.join(Workdir.wdr, base, path)
        if not os.path.exists(pth):
            return False
        obj = Cache.get(pth)
        if obj:
            return obj
        obj = Data()
        cls.read(obj, pth, base)
        return obj

    @classmethod
    def ident(cls, obj):
        "return ident string for object."
        return os.path.join(Method.fqn(obj), *str(datetime.datetime.now()).split())

    @classmethod
    def read(cls, obj, path, base="store"):
        "read object from path."
        if cls.disable:
            raise NoDisk
        with cls.lock:
            pth = os.path.join(Workdir.wdr, base, path)
            if not os.path.exists(pth):
                return False
            with open(pth, "r", encoding="utf-8") as fpt:
                try:
                    Method.update(obj, JSON.load(fpt))
                except json.decoder.JSONDecodeError as ex:
                    raise DecodeError(Utils.strip(pth)) from ex
            Cache.add(pth, obj)
            return True

    @classmethod
    def write(cls, obj, path="", base="store", skip=False):
        "write object to disk."
        if cls.disable:
            raise NoDisk
        with cls.lock:
            if path == "":
                path = cls.ident(obj)
            pth = os.path.join(Workdir.wdr, base, path)
            Utils.cdir(pth)
            with open(pth, "w", encoding="utf-8") as fpt:
                JSON.dump(obj, fpt, indent=4)
            Cache.sync(path, obj)
            return path


def __dir__():
    return (
        'Disk',
    )
