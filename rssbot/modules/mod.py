# This file is placed in the Public Domain.


"show available modules."


import os


from ..main import Commands


def mod(event):
    "show available modules."
    path = os.path.dirname(__file__)
    mods = []
    for mdd in os.listdir(path):
        if mdd == "face.py":
            continue
        if mdd.startswith("__"):
            continue
        if mdd.endswith("~"):
            continue
        mods.append(mdd[:-3])
    event.reply(",".join(sorted(mods)))


Commands.add(mod)
