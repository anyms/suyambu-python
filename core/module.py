#!/usr/bin/env python3
# coding=utf-8

"""
Copyright (c) 2019 suyambu developers (http://suyambu.spidy.app)
See the file 'LICENSE' for copying permission
"""


class Exploit:
    def __init__(self):
        self.name = None
        self.author = []
        self.description = None
        self.license = "MIT"

    def do_exploit(self, line):
        self.exploit()

    def exploit(self):
        pass
