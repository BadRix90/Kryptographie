#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, Extension

modul = Extension("chiffre", sources=["chiffre.c"])
setup(
     name = "PyChiffre",
     version = "1.0",
     description = "Module for encryption techniques.",
     ext_modules = [modul]
     )

