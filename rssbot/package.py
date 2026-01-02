# This file is placed in the Public Domain.


"module management"


import importlib.util
import os


from .command import scan
from .configs import Config
from .utility import spl


class Mods:

    dirs = {}
    modules = {}


def addpkg(*pkgs):
    "register package directory."
    for pkg in pkgs:
        dirs(pkg.__name__, pkg.__path__[0])


def dirs(name, path):
    "add module directory."
    Mods.dirs[name] = path


def getmod(name):
    "import module by name." 
    if name in spl(Config.ignore):
        return None
    if name in Mods.modules:
        return Mods.modules[name]
    mname = ""
    pth = ""
    for packname, path in Mods.dirs.items():
        modpath = os.path.join(path, name + ".py")
        if os.path.exists(modpath):
            pth = modpath
            mname = f"{packname}.{name}"
            break
    return importer(mname, pth)


def importer(name, pth=""):
    "import module by path."
    if pth and os.path.exists(pth):
        spec = importlib.util.spec_from_file_location(name, pth)
    else:
        spec = importlib.util.find_spec(name)
    if not spec or not spec.loader:
        return None
    mod = importlib.util.module_from_spec(spec)
    if not mod:
        return None
    Mods.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def mods(names):
    "list of named modules."
    return [
        getmod(x) for x in sorted(spl(names))
        if x not in spl(Config.ignore)
        or x in spl(Config.sets.init)
    ]


def modules():
    "comma seperated list of available modules."
    mods = []
    for name, path in Mods.dirs.items():
        if name in spl(Config.ignore):
            continue
        if not os.path.exists(path):
            continue
        mods.extend([
            x[:-3] for x in os.listdir(path)
            if x.endswith(".py") and not x.startswith("__") and x not in spl(Config.ignore)
        ])
    return ",".join(sorted(mods))


def scanner(names=None):
    "scan named modules for commands."
    if names is None:
        names = modules()
    mods = []
    for name in spl(names):
        module = getmod(name)
        if not module:
            continue
        scan(module)
    return mods


def __dir__():
    return (
        'Mods',
        'addpkg',
        'dirs',
        'getmod',
        'importer',
        'mods',
        'modules',
        'scanner'
    )
