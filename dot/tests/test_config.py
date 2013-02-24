#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
   dot.tests.test_config
   ~~~~~~~~~~~~~~~~~~~~~

"""

import mock
import unittest

import json
import os
import shutil
import tempfile

from dot.config import Config


class CreateTest(unittest.TestCase):
    """Creates new files or directories if needed"""

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        with mock.patch.dict('os.environ', {'HOME': self.tempdir}):
            self.config = Config(None, None)

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_no_config_exists(self):
        self.config.create()

        with open(self.config.current()['config']) as f:
            config = json.load(f)

            self.assertEqual(self.config.current(), config)

    def test_config_exists(self):
        with open(self.config.current()['config'], 'w') as f:
            f.write('{"config": "myconf", "local": "myrepo", "remote": ""}\n')

        self.config.create()

        with open(self.config.current()['config']) as f:
            config = json.load(f)

            self.assertNotEqual(self.config.current(), config)


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

