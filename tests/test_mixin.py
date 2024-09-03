# This file is placed in the Public Domain.
# pylint: disable=R0903


"mixin"


import unittest


from rssbot.object import Object


class Mix:

    "Mix"

    a = "b"


class Mixin(Mix, Object):

    "Mixin"


class TestMixin(unittest.TestCase):

    "TestMixin"

    def test_mixin(self):
        "mixin test."
        mix = Mixin()
        self.assertTrue(isinstance(mix, Mixin))
