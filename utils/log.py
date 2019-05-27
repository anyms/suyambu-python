# !/usr/bin/env python
# coding=utf-8

"""
Copyright (c) 2018 suyambu developers (http://codeinside.me/suyambu)
See the file 'LICENSE' for copying permission
"""

from utils.data_types import *


class Log:
    def __init__(self):
        self.logger = open("debug.log", "a+")

    def status(self, s):
        self.logger.write("[*] {}\n".format(s))
        print("{} {}".format(Str("[*]").blue(), s))

    def success(self, s):
        self.logger.write("[+] {}\n".format(s))
        print("{} {}".format(Str("[+]").green(), s))

    def error(self, s):
        self.logger.write("[-] {}\n".format(s))
        print("{} {}".format(Str("[-]").blue(), s))

    def warning(self, s):
        self.logger.write("[!] {}\n".format(s))
        print("{} {}".format(Str("[!]").yellow(), s))
