# This file is placed in the Public Domain.


"pool of runners"


import os


class Pool:

    def __init__(self, clazz=None):
        self.clazz = clazz or Runner()
        self.runners = []
        self.max = os.cpu_count()
        self.nrcpu = 1
        self.nrlast = 0

    def add(self, client):
        "add a runner."
        self.runners.append(client)

    def busy(self):
        for runner in self.runners:
            if runner.queue.qsize():
                return True
        return False

    def init(self, nr):
        "initialze a number of runners."
        for x in range(nr):
            runner = self.clazz()
            runner.start()
            self.add(runner)

    def put(self, *args):
        "push job to a runner."
        if not self.runners:
            return
        if self.nrlast > self.nrcpu-1:
            self.nrlast = 0
        clt = self.runners[self.nrlast]
        clt.put(*args)
        self.nrlast += 1


def __dir__():
    return (
        'Pool',
    )
