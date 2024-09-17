# This module is placed in the Public Domain.


"uptime"


import time


from ..main import STARTTIME, Commands, laps


def upt(event):
    "show uptime."
    event.reply(laps(time.time()-STARTTIME))


Commands.add(upt)
