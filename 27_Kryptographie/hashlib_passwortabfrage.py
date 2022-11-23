#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

pwhash = "578127b714de227824ab105689da0ed2"

m = hashlib.md5(bytes(input("Ihr Passwort bitte: "), "utf-8"))
if pwhash == m.hexdigest():
    print("Zugriff erlaubt")
else:
    print("Zugriff verweigert")
