# This file is placed in the Public Domain.
# pylint: disable=C0116,E0402


"fleet"


from ..objects import fmt
from ..threads import name
from ..clients import Fleet


def flt(event):
    bots = Fleet.bots.values()
    try:
        event.reply(fmt(list(Fleet.bots.values())[int(event.args[0])]))
    except (KeyError, IndexError, ValueError):
        event.reply(",".join([name(x).split(".")[-1] for x in bots]))
