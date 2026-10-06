# This file is placed in the Public Domain.


"show uptime"


import time


from rssbot.defines import Time


def upt(msg):
    "show uptiome."
    msg.reply(Time.elapsed(time.time()-Time.starttime))
