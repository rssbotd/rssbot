# This file is placed in the Public Domain.


"clients"


import threading


from .brokers import Broker
from .display import Display
from .engines import Engine
from .outputs import Output


class Buffer(Engine, Output):

    def __init__(self):
        Engine.__init__(self)
        Output.__init__(self)
        Broker.add(self)

    def raw(self, text):
        "raw output."
        raise NotImplementedError

    def start(self, daemon=True):
        "start output loop."
        Engine.start(self)
        Output.start(self, daemon=daemon)

    def stop(self):
        "stop output loop."
        Engine.stop(self)
        Output.stop(self)


class Client(Engine, Display):

    def __init__(self):
        Engine.__init__(self)
        Display.__init__(self)

    def raw(self, text):
        "raw output."
        raise NotImplementedError


class Clients:

    @staticmethod
    def announce(txt):
        "announce text on all clients."
        for obj in Broker.objs("announce"):
            obj.announce(txt)

    @staticmethod
    def display(evt):
        "display results."
        bot = Broker.get(evt.orig)
        if bot:
            bot.display(evt)

    @staticmethod
    def shutdown():
        "call stop on clients."
        for client in Broker.objs("wait"):
            client.wait()
        time.sleep(0.01)
        for client in Broker.objs("stop"):
            client.stop()
        time.sleep(0.01)


def __dir__():
    return (
        'Buffer',
        'Client',
        'Clients'
    )
