# This file is placed in the Public Domain.


"methods"


import unittest


from bigtalk.methods import Methods
from bigtalk.objects import Object


class TestMethods(unittest.TestCase):

    def testformat(self):
        o = Object()
        o.a = "b"
        self.assertEqual(Methods.fmt(o), 'a="b"')
