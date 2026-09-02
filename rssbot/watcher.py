# This file is placed in the Public Domain.


"watching files"


import errno
import logging
import os
import select
import threading
import time


from .threads import Thread


e = os.path.exists


class Watcher:

    cbs = {}
    fds = {}
    paths = {}
    running = threading.Event()

    @classmethod
    def add(cls, path, callback):
        "add callback"
        if not e(path):
            return
        file = open(path, "a+", encoding="utf-8")
        file.seek(0)
        fno = file.fileno()
        cls.paths[fno] = path
        cls.fds[fno] = file
        cls.cbs[fno] = callback
        
    @classmethod
    def callback(cls, fd):
        "run cacllback passing the filedescriptor."
        cls.cbs[fd](cls.fds[fd])

    @classmethod
    def error(cls, fds):
        "handle errors"

    @classmethod
    def loop(cls):
        "loop select."
        while cls.running.isSet():
            try:
                (inp, _out, err) = select.select(list(cls.fds.keys()), [], [])
            except OSError as ex:
                if ex.errno == errno.EBADF:
                    time.sleep(0.1)
                else:
                    logging.exception(ex)
            except Exception as ex:
                logging.exception(ex)
            time.sleep(1.0)
            if err:
                cls.error(err)
            elif inp:
                cls.input(inp)

    @classmethod
    def input(cls, fds):
        "reads changed file descriptors."
        for fd in fds:
            try:
                cls.callback(fd)
            except OSError as ex:
                if ex.errno == errno.EBADF:
                    time.sleep(0.1)
                else:
                    logging.exception(ex)
            except Exception as ex:
                logging.exception(ex)

    @classmethod
    def start(cls):
        "start watcher"
        if cls.running.isSet():
            return
        cls.running.set()
        logging.warn("watching %s", ".".join([os.path.basename(x) for x in cls.paths.values()]))
        Thread.launch(cls.loop, name="Watcher.loop")

    @classmethod
    def stop(cls):
        "stop watcher."
        cls.running.clear()


def __dir__():
    return (
        'Watcher',
    )
