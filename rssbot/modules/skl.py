# This file is placed in the Public Domain.


"skel"


import getpass


from rssbot.config  import Config
from rssbot.persist import skel
from rssbot.utils   import privileges


Cfg = Config()


def skl(event):
    privileges(getpass.getuser())
    skel()
