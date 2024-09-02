# This file is placed in the Public Domain.
# pylint: disable=C,I,R


"skel"


import getpass


from ..workdir import skel
from ..utils   import privileges


def skl(event):
    "create directories."
    privileges(getpass.getuser())
    skel()
    event.nop()
