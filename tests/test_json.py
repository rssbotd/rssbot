# This file is placed in the Public Domain.
# pylint: disable=C


"json"


import unittest


from rssbot.decoder import loads
from rssbot.encoder import dumps
from rssbot.objects import Object


VALIDJSON = "{'test': 'bla'}"
VALIDPYTHON = '{"test": "bla"}'


class TestDecoder(unittest.TestCase):

    def test_loads(self):
        obj = Object()
        obj.test = "bla"
        oobj = loads(dumps(obj))
        self.assertEqual(oobj.test, "bla")


class TestEncoder(unittest.TestCase):

    def test_dumps(self):
        obj = Object()
        obj.test = "bla"
        self.assertEqual(dumps(obj), VALIDPYTHON)
