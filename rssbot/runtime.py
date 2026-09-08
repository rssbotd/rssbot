# This file is placed in the Public Domain.


from .configs import Main
from .options import Arguments
from .kernels import Kernel
from .scripts import Scripts


def main():
    "main"
    Arguments.getargs()
    if Main.console:
        Kernel.wrap(Scripts.console)
    elif Main.service:
        Kernel.wrap(Scripts.service)
    elif Main.daemon:
        Kernel.wrap(Scripts.background)
    else:
        Kernel.wrap(Scripts.control)


def __dir__():
    return (
        'main',
    )
