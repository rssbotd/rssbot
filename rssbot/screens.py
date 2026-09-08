# This file is placed in the Public Domain.


"output to screen"


from .display import Display
from .handler import Handler


class Screen(Handler, Display):

    def __init__(self):
        Handler.__init__(self)
        Display.__init__(self)

    def raw(self, text):
        "raw output."
        raise NotImplementedError


def __dir__():
    return (
        'Screen',
    )
