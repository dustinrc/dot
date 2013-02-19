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


class CurrentTest(unittest.TestCase):
    """Current config is correct"""

    def setUp(self):
        with mock.patch.dict('os.environ', {'HOME': '/tmp'}):
            self.config = Config(None, None)

    def test_defaults(self):
        expected = {
            'rc': '/tmp/.dotrc',
            'repo': '/tmp/.dot',
        }
        actual = self.config.current()

        self.assertEqual(expected, actual)

    def test_updates(self):
        expected = {
            'rc': '/some/path/dotrc',
            'repo': '/another/path/dot_repo',
        }
        actual = self.config.current(**expected)

        self.assertEqual(expected, actual)

