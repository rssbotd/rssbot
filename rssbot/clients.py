# This file is placed in the Public Domain.


"clients"


from .brokers import Broker


class Clients:

    @staticmethod
    def announce(txt):
        "announce text on all clients."
        for obj in Broker.objs("announce"):
            obj.announce(txt)

    @staticmethod
    def display(evt):
        "display results."
        bot = Broker.get(evt.orig)
        if bot:
            bot.display(evt)

    @staticmethod
    def shutdown():
        "call stop on clients."
        for client in Broker.objs("wait"):
            try:
                client.wait()
            except (KeyboardInterrupt, EOFError):
                pass
        time.sleep(0.01)
        for client in Broker.objs("stop"):
            try:
                client.stop()
            except (KeyboardInterrupt, EOFError):
                pass
        time.sleep(0.01)


def __dir__():
    return (
        'Clients',
    )
