# This file is placed in the Public Domain.


"buffered clients"


from .outputs import Output
from .screens import Screen


class Buffer(Screen, Output):

    def __init__(self):
        Screen.__init__(self)
        Output.__init__(self)

    def raw(self, text):
        "raw output."
        raise NotImplementedError

    def start(self, daemon=True):
        "start output loop."
        Screen.start(self)
        Output.start(self, daemon=daemon)

    def stop(self):
        "stop output loop."
        Screen.stop(self)
        Output.stop(self)


def __dir__():
    return (
        'Buffer',
    )
