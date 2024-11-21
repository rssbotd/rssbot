# This file is placed in the Public Domain.
# pylint: disable=C,W0212


"service"


import getpass
import os
import pwd


from .modules import irc, rss
from .persist import pidfile, pidname
from .runtime import forever, wrap


def privileges():
    pwnam2 = pwd.getpwnam(getpass.getuser())
    os.setgid(pwnam2.pw_gid)
    os.setuid(pwnam2.pw_uid)


def main():
    privileges()
    pidfile(pidname("rssbot"))
    rss.init()
    irc.init()
    forever()


if __name__ == "__main__":
    wrap(main)
