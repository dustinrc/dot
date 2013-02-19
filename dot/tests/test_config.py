#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
   dot.tests.test_config
   ~~~~~~~~~~~~~~~~~~~~~

"""

import mock
import unittest

import os

from dot.config import Config


class DefaultsTest(unittest.TestCase):
    """Config defaults are correct"""

    def setUp(self):
        with mock.patch.dict('os.environ', {'HOME': '/tmp'}):
            self.config = Config(None, None)

    def test_no_kwargs(self):
        expected = {
            'rc': '/tmp/.dotrc',
            'repo': '/tmp/.dot',
        }
        actual = self.config.defaults()

        self.assertEqual(expected, actual)

