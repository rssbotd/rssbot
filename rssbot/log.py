# This file is placed in the Public Domain.
# pylint: disable=C,I,R,E1102


"logging"


class Logging:

    "Logging"

    filter = []
    out    = None


def debug(txt):
    "print to console."
    for skp in Logging.filter:
        if skp in txt:
            return
    if Logging.out:
        Logging.out(txt)


def __dir__():
    return (
        'Logging',
        'debug'
    )
