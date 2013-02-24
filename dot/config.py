#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
   dot.config
   ~~~~~~~~~~

"""


from json import dump
from os import environ
from os.path import abspath, exists, join as op_join

from cliff.command import Command


class Config(Command):
    """Initialization and settings."""

    def __init__(self, app, app_args):
        super(Config, self).__init__(app, app_args)
        self._current = {
            'config': abspath(op_join(environ['HOME'], '.dotrc')),
            'local': abspath(op_join(environ['HOME'], '.dot')),
            'remote': '',
        }

    def take_action(self, parsed_args):
        return NotImplemented

    def create(self):
        """Creates any files or directories needed by default."""

        if not exists(self._current['config']):
            with open(self._current['config'], 'w') as f:
                dump(self._current, f)

    def current(self, **kwargs):
        """Returns the current configurations.  If keyword arguments
        are given, it will update the current dictionary before returning it.
        """

        self._current.update(kwargs)
        return self._current

