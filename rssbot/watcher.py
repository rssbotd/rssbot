# This file is placed in the Public Domain.


"watching files"


import io
import logging
import os
import select
import threading
import time


from .encoder import JSONL
from .threads import Thread


class Watcher:

    cbs = {}
    fds = {}
    running = threading.Event()

    @classmethod
    def add(cls, path, callback):
        "add callback"
        logging.warn("add %s", path)
        file = open(path, "r", encoding="utf-8")
        file.seek(0, 2)
        cls.fds[file.fileno()] = file
        cls.cbs[file.fileno()] = callback        
        
    @classmethod
    def callback(cls, fd):
        "run cacllback passing the filedescriptor."
        cls.cbs[fd](fd)

    @classmethod
    def err(cls, fds):
        "handle errors"

    @classmethod
    def loop(cls):
        "loop select."
        while cls.running.isSet():
            try:
                (inp, _out, err) = select.select(list(cls.fds.keys()), [], [])
            except OSError as ex:
                if "Bad file" in str(ex):
                    time.sleep(60.0)
                else:
                    logging.exception(ex)
                continue
            if err:
                logging.error(err)
            elif inp:
                cls.input(inp)

    @classmethod
    def input(cls, fds):
        "reads changed file descriptors."
        for fd in fds:
            cls.callback(fd)

    @classmethod
    def start(cls):
        "start watcher"
        if cls.running.isSet():
            return
        cls.running.set()
        logging.warn("starting watcher")
        Thread.launch(cls.loop, name="Watcher.loop")

    @classmethod
    def stop(cls):
        "stop watcher."
        self.running.clear()


def __dir__():
    return (
        'Watcher',
    )
