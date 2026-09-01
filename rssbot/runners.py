# This file is placed in the Public Domain.


"pool of clients"


import threading


class Runners:

    runners = []
    lock = threading.RLock()
    nrcpu = 1
    nrlast = 0

    @classmethod
    def add(cls, client):
        "add a runner."
        cls.runners.append(client)

    @classmethod
    def init(cls, nrcpu, clazz):
        "initialize a runner."
        cls.nrcpu = nrcpu
        for _x in range(cls.nrcpu):
            clt = clazz()
            clt.start()
            Runners.add(clt)

    @classmethod
    def put(cls, *args):
        "push job to a runner."
        if not cls.runners:
            cls.init(Runners.nrcpu, Runner)
        with cls.lock:
            if cls.nrlast >= cls.nrcpu-1:
                cls.nrlast = 0
            clt = cls.runners[cls.nrlast]
            clt.put(*args)
            cls.nrlast += 1


def __dir__():
    return (
        "Runners",
    )
