#!/usr/bin/env python
# coding=utf-8

"""
Copyright (c) 2018 suyambu developers (http://codeinside.me/suyambu)
See the file 'LICENSE' for copying permission
"""

import os

from utils import log
from utils.data_types import *
from core.shell import Shell


class SuyambuShell(Shell):
    def __init__(self):
        Shell.__init__(self)
        self.update_prompt("~")

    def update_prompt(self, s):
        self.prompt = "suyambu ({}) : ".format(Str(s).red())
