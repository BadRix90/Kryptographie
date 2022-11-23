#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import hashlib

with open("datei1.txt", "rb") as f1, open("datei2.txt", "rb") as f2:
    if hashlib.md5(f1.read()).digest() == hashlib.md5(f2.read()).digest():
        print("Die Dateien sind gleich")
    else:
        print("Die Dateien sind verschieden")
