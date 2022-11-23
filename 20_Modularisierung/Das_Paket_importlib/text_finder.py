#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import imp

class TextLoader:
    def __init__(self, path):
        pass
        
    def load_module(self, fullname):
        if fullname in sys.modules:
            return sys.modules[fullname]
        else:
            module = imp.new_module(fullname)
            sys.modules[fullname] = module
            
        module.__file__ = fullname + ".txt"
        module.__name__ = fullname
        module.__package__ = ""
        module.__loader__ = self
        
        try:
            with open(fullname + ".txt") as f:
                module.text = f.read()
            return module
        except FileNotFoundError:
            del sys.modules[fullname]
            raise ImportError

class TextFinder:
    def __init__(self, path):
        if path != "#":
            raise ImportError
    
    def find_module(self, fullname, path=None):
        try:
            open(fullname + ".txt").close()
            return TextLoader(path)
        except FileNotFoundError:
            return None
    
sys.path_hooks.append(TextFinder)
sys.path.append("#")

# Test
import testdatei
print(testdatei.text)
