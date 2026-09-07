# This file is placed in the Public Domain.


"output to screen"


from .display import Display
from .engines import Engine


class Screen(Engine, Display):

    def __init__(self):
        Engine.__init__(self)
        Display.__init__(self)

    def raw(self, text):
        "raw output."
        raise NotImplementedError


def __dir__():
    return (
        'Screen',
    )
