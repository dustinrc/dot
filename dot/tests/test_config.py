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
            'config': '/tmp/.dotrc',
            'local': '/tmp/.dot',
            'remote': '',
        }
        actual = self.config.current()

        self.assertEqual(expected, actual)

    def test_updates(self):
        expected = {
            'config': '/some/path/dotrc',
            'local': '/another/path/dot_repo',
            'remote': 'https://github.com/dustinrc/dotfiles.git',
        }
        actual = self.config.current(**expected)

        self.assertEqual(expected, actual)

