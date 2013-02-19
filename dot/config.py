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

    def take_action(self, parsed_args):
        return NotImplemented

    @staticmethod
    def defaults(**kwargs):
        defaults = {
            'rc': os.path.abspath(os.path.join(os.environ['HOME'], '.dotrc')),
            'repo': os.path.abspath(os.path.join(os.environ['HOME'], '.dot')),
        }

        return defaults

