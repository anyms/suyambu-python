#!/usr/bin/env python3
# coding=utf-8

"""
Copyright (c) 2019 suyambu developers (http://suyambu.spidy.app)
See the file 'LICENSE' for copying permission
"""

from fancycmd.data_types import *
import os

from core.shell import Shell
from utils.log import Log


class Suyambu(Shell):
    def __init__(self):
        Shell.__init__(self)
        self.update_prompt("~")
        
        self.abspath = os.path.dirname(os.path.abspath(__file__))
        self.modules = {}
        self.module_names = []
        self.log = Log()

        self.initiate_modules()
        self.module = None

    def initiate_modules(self):
        for path, dirs, files in os.walk("{}/modules".format(self.abspath)):
            root_path = "modules" + path.split("modules")[1]
            if "__" not in root_path:
                for f in files:
                    module_path = "{}/{}".format(path, f)
                    module_str = "{}.{}".format(root_path.replace("/", "."), f.replace(".py", ""))
                    
                    mod_file = open(module_path, "rt", encoding="iso-8859-15")
                    data = mod_file.read()
                    mod_file.close()

                    if "SuyambuModule" in data:
                        module = __import__(module_str, fromlist=["SuyambuModule"]).SuyambuModule()
                        nodes = module_str.replace("modules.", "").split(".")
                        name = self.format_module_name("{}".format("/".join(nodes)))
                        self.module_names.append(name)
                        self.modules[name] = module

    def format_module_name(self, name, is_real=False):
        return name.replace("exploits/", "exploit/").replace("payloads/", "payload/").replace("encoders/", "encoder/")

    def update_prompt(self, module):
        if module == "~":
            self.prompt = "{} ➜ ".format(Str("suyambu").yellow())
        else:
            self.prompt = "{} ({}) ➜ ".format(Str("suyambu").yellow(), Str(module).green())

    def do_help(self, line):
        print(__doc__)

    def do_use(self, line):
        try:
            self.module = self.modules[line]
            self.update_prompt(line)
        except:
            self.log.error("unknown module '{}'".format(line))

    def default(self, line):
        if "do_" + line in dir(self.module):
            getattr(self.module, "do_" + line)(line)


if __name__ == '__main__':
    suyambu = Suyambu()
    suyambu.mainloop()
