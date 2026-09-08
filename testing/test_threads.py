# This file is placed in the Public Domain.


"threading"


import unittest


from rssbot.defines import Thr


def func():
    return "ok"


class TestThread(unittest.TestCase):

    def test_task(self):
        task = Thr(func)
        task.start()
        result = task.join()
        self.assertEqual(result, "ok")
