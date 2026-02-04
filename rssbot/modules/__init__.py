# This file is placed in the Public Domain.


"modules"


from rssbot.objects import Default


class Config(Default):

    pass


Cfg = Config()


def __dir__():
    return (
        'Cfg',
    )
