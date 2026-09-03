# This file is placed in the Public Domain.


"clients"


import os
import threading
import time


class Clients:

    clients = {}
    max = os.cpu_count()
    nrcpu = 1
    nrlast = 0

    @classmethod
    def add(cls, client):
        "add a runner."
        cls.clients[repr(client)] = client

    @classmethod
    def announce(cls, txt):
        "announce text on all clients."
        for obj in cls.clients.values():
            obj.announce(txt)

    @classmethod
    def display(cls, evt):
        "display results."
        bot = cls.clients.get(evt.orig, None)
        if bot:
            bot.display(evt)

    @classmethod
    def get(cls, orig):
        "return client by origin."
        return cls.clients.get(orig)

    @classmethod
    def put(cls, *args):
        "push job to a runner."
        if not cls.clients:
            return
        if cls.nrlast > cls.nrcpu-1:
            cls.nrlast = 0
        print(len(cls.clients))
        clt = list(cls.clients.values())[cls.nrlast]
        clt.put(*args)
        cls.nrlast += 1

    @classmethod
    def shutdown(cls):
        "call stop on clients."
        for client in cls.clients.values():
            try:
                client.wait()
            except (KeyboardInterrupt, EOFError):
                pass
            time.sleep(0.01)
            try:
                client.stop()
            except (KeyboardInterrupt, EOFError):
                pass
            time.sleep(0.01)


def __dir__():
    return (
        'Clients',
    )
