#!/usr/bin/env python
# coding=utf-8

"""
Copyright (c) 2018 suyambu developers (http://codeinside.me/suyambu)
See the file 'LICENSE' for copying permission
"""

from cmd import Cmd
import os

from utils import log
from utils.data_types import Str


class Prompt(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "prompt ({}) > ".format(Str("home").red())

    def emptyline(self):
        pass


prompt = Prompt()
prompt.cmdloop()
