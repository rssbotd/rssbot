# This file is placed in the Public Domain.


"clients"


import threading
import time


from .brokers import Broker
from .engines import Engine
from .outputs import Output


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


class Display:

    block = threading.Event()

    def __init__(self):
        super().__init__()
        self.olock = threading.RLock()
        self.silent = False
        Broker.add(self)

    def announce(self, text):
        "announce text to all channels."
        if not self.silent:
            self.raw(text)

    def display(self, event):
        "display event results."
        with self.olock:
            for txt in event.result:
                if self.block.is_set():
                    return
                self.dosay(event.channel, txt)

    def dosay(self, channel, text):
        "say called by display."
        self.say(channel, text)

    def raw(self, text):
        "raw output."
        raise NotImplementedError

    def say(self, channel, text):
        "say text in channel."
        self.raw(text)


class Client(Engine, Display):

    def __init__(self):
        Engine.__init__(self)
        Display.__init__(self)

    def raw(self, text):
        "raw output."
        raise NotImplementedError


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


def __dir__():
    return (
        'Buffer',
        'Client',
        'Clients',
        'Display'
    )
