# This file is placed in the Public Domain.


"skel"


import getpass


from ..config  import Config
from ..persist import skel
from ..utils   import privileges


Cfg = Config()


def skl(event):
    "create directories."
    privileges(getpass.getuser())
    skel()
    event.nop()
