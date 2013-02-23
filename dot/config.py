#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
   dot.config
   ~~~~~~~~~~

"""


import os

from cliff.command import Command


class Config(Command):
    """Initialization and settings."""

    def __init__(self, app, app_args):
        super(Config, self).__init__(app, app_args)
        self._current = {
            'config': os.path.abspath(os.path.join(os.environ['HOME'],
                                                   '.dotrc')),
            'local': os.path.abspath(os.path.join(os.environ['HOME'], '.dot')),
            'remote': '',
        }

    def take_action(self, parsed_args):
        return NotImplemented

    def current(self, **kwargs):
        """Returns the current configurations.  If keyword arguments
        are given, it will update the current dictionary before returning it.
        """

        self._current.update(kwargs)
        return self._current

