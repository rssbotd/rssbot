# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W0201


"configuration"


import os


from .default import Default
from .workdir import Workdir


class Config(Default):

    "Config"


    name    = Workdir.__module__.rsplit(".", maxsplit=2)[-2]
    wdr     = os.path.expanduser(f"~/.{name}")
    pidfile = os.path.join(wdr, f"{name}.pid")


def __dir__():
    return (
        "Config",
        'boot'
    )
