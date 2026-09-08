# This file is placed in the Public Domain.


"callback engine"


import queue
import threading


from .looping import Loop
from .threads import Thread


class Engine(Loop):

    def __init__(self):
        Loop.__init__(self)
        self.cbs = {}
        self.queue = queue.Queue()
        self.stopped = threading.Event()
        self.done = threading.Event()

    def handle(self, *args):
        "run callback function with event."
        if not args:
            return
        event = args[0]
        func = self.cbs.get(event.kind, None)
        if not func:
            event.ready()
            return
        event._thr = Thread.launch(func, *args)

    def register(self, kind, callback):
        "register callback."
        self.cbs[kind] = callback


def __dir__():
    return (
        'Engine',
    )
