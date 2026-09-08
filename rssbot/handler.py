# This file is placed in the Public Domain.


"stuck in a loop"


from .engines import Engine


class Handler(Engine):

    def after(self, event):
        "called after callback."

    def loop(self):
        "callback loop."
        while not self.stopped.is_set():
            self.poll()
            args = self.queue.get()
            if args[0] is None:
                self.queue.task_done()
                break
            self.handle(*args)
            self.after(*args)
            self.queue.task_done()
        self.done.set()

    def poll(self):
        "create event and put it on the queue."


def __dir__():
    return (
        'Handler',
    )
