#!/usr/bin/env python
# coding=utf-8

"""
Copyright (c) 2018 suyambu developers (http://codeinside.me/suyambu)
See the file 'LICENSE' for copying permission
"""

from fancycmd import Cmd
import os

from utils import log


class Shell(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "shell > "

    def emptyline(self):
        pass
