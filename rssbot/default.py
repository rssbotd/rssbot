# This file is placed in the Public Domain.
# pylint: disable=C,I,R


"default values"


from .object import Object


class Default(Object):

    "Default"

    def __getattr__(self, key):
        return self.__dict__.get(key, "")


def __dir__():
    return (
        'Default',
    )
