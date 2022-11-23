#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

setup(
     name = "calc",
     version = "1.0",
     executables = [Executable("calc.py")]
     )
