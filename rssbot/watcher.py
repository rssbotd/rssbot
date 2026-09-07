# This file is placed in the Public Domain.


"watching files"


import os
import threading
import time


from .loopers import Loop


e = os.path.exists


class Watcher(Loop):

    running = threading.Event()
    sleep = 1.0
    cbs = {}
    times = {}

    def add(self, path, callback):
        "add callback"
        if not os.path.exists(path):
            return
        self.cbs[path] = callback

    def callback(self, path):
        "run callback."
        self.cbs[path]()

    def init(self, times={}):
        "read timestamps."
        for path in self.cbs:
            if not e(path):
                continue
            self.times[path] = times.get(path, os.stat(path).st_mtime)

    def loop(self):
        "loop select."
        while self.running.isSet():
            for path in self.cbs:
                if not e(path):
                    continue
                mtime = os.stat(path).st_mtime
                if mtime > self.times[path]:
                    self.callback(path)
                self.times[path] = mtime
            time.sleep(self.sleep)


def __dir__():
    return (
        'Watcher',
    )
