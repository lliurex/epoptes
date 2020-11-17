# This file is part of Epoptes, https://epoptes.org
# Copyright 2018 the Epoptes team, see AUTHORS.
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Similar to logging.Logger, but simpler.
"""
# TODO: implement debug levels and environment interface.
import os
import sys


class Logger:
    """Similar to logging.Logger, but simpler."""
    def __init__(self, name=None, file=sys.stderr):
        """Check if debugging is activated for "name"."""
        debug = os.getenv('DEBUG', '')
        if debug and name.endswith(debug):
            func = self.stderr
        else:
            func = self.null
        # debug, info, warning, error, critical
        self.d = func
        self.i = func
        self.w = self.stderr
        self.e = self.stderr
        self.c = self.stderr
        self.file = file

    def null(self, *_args, end='\n'):
        """The self.[cdeiw] variables point here when debugging is disabled."""
        pass

    def stderr(self, *args, end='\n'):
        """The self.[cdeiw] variables point here when debugging is enabled."""
        if self:
            print(*args, end=end, file=self.file)
