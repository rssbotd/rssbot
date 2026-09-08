# This file is placed in the Public Domain.


"stuck in a loop"


import inspect
import logging
import os
import queue
import threading
import time
import _thread


e = os.path.exists


class Loop:

    def __init__(self):
        self.queue = queue.Queue()
        self.stopped = threading.Event()
        self.done = threading.Event()

    def handle(self, event):
        "handle event."

    def loop(self):
        "callback loop."
        while not self.stopped.is_set():
            event = self.queue.get()
            if event is None:
                break
            self.handle(event)
        self.done.set()

    def put(self, event):
        "put event on queue."
        self.queue.put(event)

    def start(self, daemon=True):
        "start callback loop."
        self.done.clear()
        self.stopped.clear()
        Thread.launch(self.loop, daemon=daemon)

    def stop(self):
        "stop xallback loop."
        self.stopped.set()
        self.queue.put(None)
        self.done.wait()

    def wait(self):
        "wait for all events to finish,"
        try:
            self.queue.join()
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()


class Engine(Loop):

    def __init__(self):
        Loop.__init__(self)
        self.cbs = {}
        self.queue = queue.Queue()
        self.stopped = threading.Event()
        self.done = threading.Event()

    def handle(self, event):
        "run callback function with event."
        func = self.cbs.get(event.kind, None)
        if not func:
            event.ready()
            return
        event._thr = Thread.launch(func, event)

    def register(self, kind, callback):
        "register callback."
        self.cbs[kind] = callback


class Handler(Engine):

    def after(self, event):
        "called after callback."

    def loop(self):
        "callback loop."
        while not self.stopped.is_set():
            self.poll()
            event = self.queue.get()
            if event is None:
                self.queue.task_done()
                break
            event.orig = repr(self)
            self.handle(event)
            self.after(event)
            self.queue.task_done()
        self.done.set()

    def poll(self):
        "create event and put it on the queue."


class Repeater(Loop):

    counter = 0
    running = threading.Event()
    stopped = threading.Event()
    todo = {}

    def add(self, sleep, func, *args, **kwargs):
        "add a repeater."
        if not self.stopped.is_set():
            self.start()
        sleep = str(sleep)
        if sleep not in self.todo:
            self.todo[sleep] = []
        self.todo[sleep].append((func, args, kwargs))

    def loop(self):
        "repeater loop."
        while not self.stopped.is_set():
            time.sleep(1.0)
            self.counter += 1
            for sleep in self.todo:
                slept = float(sleep)
                if self.counter % slept != 0:
                    continue
                for func, args, kwargs in self.todo[sleep]:
                    Thread.launch(func, *args, **kwargs)

    def start(self, daemon=True):
        "start callback loop."
        self.done.clear()
        self.stopped.clear()
        Thread.launch(self.loop, daemon=daemon, name="Repeater.loop")


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

    def start(self, daemon=True):
        "start callback loop."
        self.done.clear()
        self.stopped.clear()
        Thread.launch(self.loop, daemon=daemon, name="Runner.loop")

class Watcher(Loop):

    sleep = 1.0
    cbs = {}
    times = {}

    def add(self, path, callback):
        "add callback"
        if not os.path.exists(path):
            return
        self.cbs[path] = callback

    def init(self, times={}):
        "read timestamps."
        for path in self.cbs:
            if not e(path):
                continue
            self.times[path] = times.get(path, os.stat(path).st_mtime)

    def loop(self):
        "loop select."
        while not self.stopped.isSet():
            for path in self.cbs:
                if not e(path):
                    continue
                mtime = os.stat(path).st_mtime
                if mtime > self.times[path]:
                    self.cbs[path]()
                self.times[path] = mtime
            time.sleep(self.sleep)


class Pool:

    def __init__(self, clazz):
        self.clazz = clazz
        self.runners = []
        self.max = os.cpu_count()
        self.nrcpu = 1
        self.nrlast = 0

    def add(self, client):
        "add a runner."
        self.runners.append(client)

    def busy(self):
        for runner in self.runners:
            if runner.queue.qsize():
                return True
        return False

    def init(self, nr):
        "initialze a number of runners."
        for x in range(nr):
            runner = self.clazz()
            runner.start()
            self.add(runner)

    def put(self, *args):
        "push job to a runner."
        if not self.runners:
            return
        if self.nrlast > self.nrcpu-1:
            self.nrlast = 0
        clt = self.runners[self.nrlast]
        clt.put(*args)
        self.nrlast += 1


class Thr(threading.Thread):

    block = threading.Event()

    def __init__(self, func, *args, daemon=True, **kwargs):
        super().__init__(None, self.run, None, (), daemon=daemon)
        self.event = None
        self.name = kwargs.get("name", Thread.name(func))
        self.queue = queue.Queue()
        self.result = None
        self.starttime = time.time()
        self.queue.put((func, args))

    def __iter__(self):
        return self

    def __next__(self):
        yield from dir(self)

    def join(self, timeout=0.0):
        "join thread and return result."
        try:
            super().join(timeout or None)
            return self.result
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()

    def run(self):
        "run function."
        func, args = self.queue.get()
        if self.block.is_set():
            return
        try:
            self.result = func(*args)
        except (KeyboardInterrupt, EOFError):
            _thread.interrupt_main()
        except Exception as ex:
            logging.exception(ex)
            _thread.interrupt_main()


class Thread:

    lock = threading.RLock()

    @classmethod
    def launch(cls, func, *args, **kwargs):
        "start a new thread running function with arguments."
        with cls.lock:
            "run function in a thread."
            task = Thr(func, *args, **kwargs)
            task.start()
            return task

    @classmethod
    def clsname(cls, obj):
        "class name of an object."
        if "__self__" in dir(obj):
            return obj.__self__.__class__.__name__
        return obj.__class__.__name_

    @classmethod
    def name(cls, obj):
        "string of function/method."
        if inspect.ismethod(obj):
            return f"{cls.clsname(obj)}.{obj.__name__}"
        if inspect.isfunction(obj):
            return repr(obj).split()[1]
        return repr(obj)


def __dir__():
    return (
        'Loop',
        'Engine',
        'Handler',
        'Pool',
        'Repeater',
        'Runner',
        'Watcher',
        'Thr',
        'Thread'
    )
