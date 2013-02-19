#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
   dot.tests.test_config
   ~~~~~~~~~~~~~~~~~~~~~

"""

import unittest

import os

from dot.config import Config


class DefaultsTest(unittest.TestCase):
    """Config defaults are correct"""

    def setUp(self):
        os.environ['HOME'] = '/tmp'
        self.defaults = Config.defaults()

    def test_rc(self):
        self.assertEqual(self.defaults['rc'], '/tmp/.dotrc')

    def test_repo(self):
        self.assertEqual(self.defaults['repo'], '/tmp/.dot')

