# This file is placed in the Public Domain.


"long time background running processes"


import os
import sys


from .persist import Workdir


class Daemon:

    @classmethod
    def daemon(cls):
        "run in the background."
        pid = os.fork()
        if pid != 0:
            os._exit(0)
        os.setsid()
        pid2 = os.fork()
        if pid2 != 0:
            os._exit(0)
        if not Main.sets.verbose:
            cls.null(sys.stdin)
            cls.null(sys.stdout)
            cls.null(sys.stderr)
        os.umask(0o077)
        os.chdir("/")
        os.nice(10)

    @classmethod
    def null(cls, io):
        "route to dev/null."
        with open('/dev/null', 'r', encoding="utf-8") as sis:
            os.dup2(sis.fileno(), io.fileno())

    @classmethod
    def pid(cls):
        return Workdir.pid(Main.name)

    @classmethod
    def privileges(cls):
        "drop privileges."
        import getpass
        import pwd
        pwnam2 = pwd.getpwnam(getpass.getuser())
        os.setgid(pwnam2.pw_gid)
        os.setuid(pwnam2.pw_uid)


def __dir__():
    return (
        'Daemon',
    )
