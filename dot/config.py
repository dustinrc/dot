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
        self._defaults = {
            'rc': os.path.abspath(os.path.join(os.environ['HOME'], '.dotrc')),
            'repo': os.path.abspath(os.path.join(os.environ['HOME'], '.dot')),
        }

    def take_action(self, parsed_args):
        return NotImplemented

    def defaults(self, **kwargs):
        """Returns the current configuration defaults.  If keyword arguments
        are given, it will update the defaults dictionary before returning it.
        """

        return self._defaults

