# This file is placed in the Public Domain.


"console"


import sys


from .cpmmand import Commands
from .message import Message
from .screens import Screen


class CLI(Screen):

    def __init__(self):
        Screen.__init__(self)
        self.register("command", Commands.command)

    def after(self, event):
        "wait for event to finish"
        event.wait()

    def raw(self, text):
        "write to console."
        print(text.encode('utf-8', 'replace').decode("utf-8"))
        sys.stdout.flush()


class Console(CLI):

    def __init__(self):
        CLI.__init__(self)
        self.silent = True

    def poll(self):
        "return event."
        evt = Message()
        evt.orig = repr(self)
        evt.text = input("> ")
        evt.kind = "command"
        self.put(evt)
        return evt


def __dir__():
    return (
       'CLI',
       'Console'
    )
