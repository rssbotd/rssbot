# This file is placed in the Public Domain.


"kernels"


import logging
import sys
import time


from .booting import Boot
from .command import Commands
from .configs import Main
from .daemons import Daemon
from .package import MisMatch, Mods
from .sources import MD5
from .workdir import Workdir


class Kernel(Boot, Daemon):

    @classmethod
    def banner(cls, force=False):
        "hello."
        if not force and not Main.verbose:
            return
        tmr = time.ctime(time.time()).replace("  ", " ")
        txt = "%s since %s %s (%s)" % (
            Main.name.upper(),
            tmr,
            Main.level.upper() or "WARNING",
            MD5.core()
        )
        print(txt.replace("  ", " "))
        sys.stdout.flush()

    @classmethod
    def boot(cls):
        cls.configure(Main)
        Mods.dir(Workdir.moddir())
        Mods.dir(Mods.moddir())
        if Main.local:
            Mods.dir("mods", "mods")
        if Main.all:
            Main.mods = ",".join(Mods.list())
        Commands.table()
        Mods.table()
        if Main.scanner or Main.local:
            Commands.scanner()

    @classmethod
    def wrap(cls, func, *args, dofinal=None):
        "restore console."
        import termios
        try:
            old = termios.tcgetattr(sys.stdin.fileno())
        except termios.error:
            old = False
        try:
            cls.wrapped(func, *args)
        except MisMatch as ex:
            logging.error("mismatch %s", ex)
        except (KeyboardInterrupt, EOFError):
            pass
        if old:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old)
        if dofinal:
            dofinal()


def __dir__():
    return (
        'Kernel',
    )
