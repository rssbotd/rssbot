# This file is placed in the Public Domain.


"long time background running processes"


import argparse
import os
import sys
import time


from .defines import Boot, Client, Cmd, Commands, Daemon, Data, Main, Md5
from .defines import Message, Mods, Method, Workdir


class Arguments:

    @classmethod
    def getargs(cls):
        "parse commandline arguments."
        Main.name = Main.name or Method.pkgname(Main)
        theparser = argparse.ArgumentParser(
            prog=Main.name,
            description=f'{Main.name.upper()}',
            epilog='use "%(prog)s cmd" for a list of commands.',
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
        group = theparser.add_mutually_exclusive_group()
        group.add_argument("-c", "--console", action="store_true", help="start a console.")
        group.add_argument("-d", "--daemon", action="store_true", help="run as background daemon.")
        group.add_argument("-s", "--service", action="store_true", help="run as service.")
        parser = theparser.add_argument_group()
        parser.add_argument("-a", "--all", action="store_true", help="load all modules.")
        parser.add_argument("-v", "--verbose", action='store_true', help='enable verbose.')
        parser.add_argument("-w", "--wait", action='store_true', help='wait for services to start.')
        optionparser = theparser.add_argument_group()
        optionparser.add_argument("-l", "--level", default="warning", help='set loglevel.', metavar="level")
        optionparser.add_argument("-m", "--mods", default="", help='modules to load.', metavar="m1,m2")
        optionparser.add_argument("-p", "--path", default='', help='path to modules directory.', metavar="path")
        optparser = theparser.add_argument_group()
        optparser.add_argument("--admin", action="store_true", help="enable admin mode.")
        optparser.add_argument("--default", default="irc,mdl,rss,wsd", help=argparse.SUPPRESS)
        optparser.add_argument("--nochdir", action="store_true", help=argparse.SUPPRESS)
        optparser.add_argument("--scanner", action="store_true", help="do full modules scan on boot.")
        optparser.add_argument("--wdr", default="", help="set modules directory.")
        args, arguments = theparser.parse_known_args()
        Main.sets = Data()
        Method.update(Main.sets, args)
        Main.otxt = " ".join(arguments)


class Kernel(Boot, Daemon):

    @classmethod
    def banner(cls, force=False):
        "hello."
        if not force and not Main.sets.verbose:
            return
        tmr = time.ctime(time.time()).replace("  ", " ")
        txt = "%s since %s %s (%s)" % (
            Main.name.upper(),
            tmr,
            Main.sets.level.upper() or "WARNING",
            Md5.core()
        )
        print(txt.replace("  ", " "))
        sys.stdout.flush()

    @classmethod
    def boot(cls):
        Arguments.getargs()
        cls.configure(Main)
        Mods.dir(Workdir.moddir())
        Mods.dir(Mods.moddir())
        Commands.add(Cmd.cmd)
        if Main.sets.all:
            Main.sets.mods = ",".join(Mods.list())
        if Main.sets.scanner or Main.sets.all:
            Commands.scanner()
        else:
            Commands.table()
        Mods.table()

    @classmethod
    def wrap(cls, func, *args, dofinal=None):
        "restore console."
        import termios
        try:
            old = termios.tcgetattr(sys.stdin.fileno())
        except termios.error:
            old = False
        cls.wrapped(func, *args)
        if old:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old)
        if dofinal:
            dofinal()


class CLI(Client):

    def __init__(self):
        Client.__init__(self)
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


class Scripts:

    @staticmethod
    def background():
        "background script."
        Kernel.daemon()
        Kernel.privileges()
        Kernel.pid()
        Main.sets.mods = ",".join(Mods.list())
        Kernel.init(Main.sets.mods)
        Kernel.forever()

    @staticmethod
    def console():
        "console script."
        import readline
        readline.redisplay()
        if Main.sets.verbose:
            Kernel.banner()
        Kernel.init(Main.sets.mods)
        csl = Console()
        csl.start()
        Kernel.forever()

    @staticmethod
    def control():
        "cli script."
        cli = CLI()
        evt = Message()
        evt.orig = repr(cli)
        evt.text = Main.otxt
        Commands.command(evt)
        evt.wait()

    @staticmethod
    def service():
        "service script."
        Kernel.privileges()
        Kernel.pid()
        if not Main.sets.verbose:
            Kernel.banner(True)
        Main.sets.mods = ",".join(Mods.list())
        Kernel.init(Main.sets.mods)
        Kernel.forever()


def main():
    "main"
    Kernel.boot()
    sys.argv[0] = Main.name
    if Main.sets.console:
        Kernel.wrap(Scripts.console)
    elif Main.sets.service:
        Kernel.wrap(Scripts.service)
    elif Main.sets.daemon:
        Kernel.wrap(Scripts.background)
    else:
        Kernel.wrap(Scripts.control)


def __dir__():
    return (
        'Arguments',
        'CLI',
        'Kernel',
        'Scripts',
        'main'
    )
