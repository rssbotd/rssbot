# This file is placed in the Public Domain.
# pylint: disable=R0902,R0903


"configuration"


import os


from .default import Default


class Config(Default):

    "Config"


    name    = Default.__module__.rsplit(".", maxsplit=2)[-2]
    wdr     = os.path.expanduser(f"~/.{name}")
    pidfile = os.path.join(wdr, f"{name}.pid")

    def __init__(self):
        Default.__init__(self)
        self.name = self.name or Config.name
        self.wdr  = self.wdr or Config.wdr
        self.pidfile = self.pidfile or Config.pidfile


def __dir__():
    return (
        "Config",
    )
