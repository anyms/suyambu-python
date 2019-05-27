#!/usr/bin/env python3
# coding=utf-8

"""
Copyright (c) 2019 suyambu developers (http://suyambu.spidy.app)
See the file 'LICENSE' for copying permission
"""

import os
import sys

try:
    import readline
except ImportError:
    pass

from utils.data_types import *


def main():
    readline.set_completer(complete)
    readline.parse_and_bind("tab: complete")

    inp = input("prompt ({}) > ".format(Str("home").red()))
    print("output: {}".format(inp))


def complete(text, status):
    if status == 0:
        origline = readline.get_line_buffer()
        line = origline.lstrip()
        stripped = len(origline) - len(line)
        begidx = readline.get_begidx() - stripped
        endidx = readline.get_endidx() - stripped

        comps = ["name", "age"]
        sys.stdout.write("\n")
        for comp in comps:
            sys.stdout.write(comp + "  ")

        sys.stdout.write("\ncmd > " + text)
        return "hello"


if __name__ == '__main__':
    main()
