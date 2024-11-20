# This file is placed in the Public Domain.
# pylint: disable=C,W0212


"daemon"


import os, sys


from .modules import face
from .persist import Workdir, pidfile, pidname


NAME        = __file__.rsplit(os.sep, maxsplit=2)[-2]
Workdir.wdr = os.path.expanduser(f"~/.{NAME}")


def daemon(verbose=False):
    pid = os.fork()
    if pid != 0:
        os._exit(0)
    os.setsid()
    pid2 = os.fork()
    if pid2 != 0:
        os._exit(0)
    if not verbose:
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), sys.stdin.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as sos:
            os.dup2(sos.fileno(), sys.stdout.fileno())
        with open('/dev/null', 'a+', encoding="utf-8") as ses:
            os.dup2(ses.fileno(), sys.stderr.fileno())
    os.umask(0)
    os.chdir("/")
    os.nice(10)


def forever():
    while True:
        try:
            time.sleep(0.1)
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()


def modloop(*pkgs, disable=""):
    for pkg in pkgs:
        for modname in dir(pkg):
            if modname in spl(disable):
                continue
            if modname.startswith("__"):
                continue
            yield getattr(pkg, modname)


def privileges():
    import getpass
    import pwd
    pwnam2 = pwd.getpwnam(getpass.getuser())
    os.setgid(pwnam2.pw_gid)
    os.setuid(pwnam2.pw_uid)


def scanner(*pkgs, init=False, disable=""):
    result = []
    for mod in modloop(*pkgs, disable=disable):
        thr = None
        if init and "init" in dir(mod):
            thr = launch(mod.init)
        result.append((mod, thr))
    return result


def main():
    if "-d" in sys.argv:
        daemon()
    privileges()
    pidfile(pidname(NAME))
    scanner(face, init=True)
    forever()


if __name__ == "__main__":
    wrap(main)
