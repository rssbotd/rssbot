# This file is placed in the Public Domain.


"run jobs"


from .looping import Loop


class Runner(Loop):

    def run(self, *args, **kwargs):
        "fetch a feed."
        raise NotImplementedError

    def loop(self):
        "loop to handle fetch jobs."
        while not self.stopped.is_set():
            job = self.queue.get()
            if job is None:
                break
            self.run(*job)


def __dir__():
    return (
        'Runner',
    )
