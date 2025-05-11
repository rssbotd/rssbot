# This file is placed in the Public Domain.


"composite"


import unittest


from rssbot.object import Object


class TestComposite(unittest.TestCase):

    def testcomposite(self):
        obj = Object()
        obj.obj = Object()
        obj.obj.abc = "test"
        self.assertEqual(obj.obj.abc, "test")
