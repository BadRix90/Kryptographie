#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

f = open("rheinwerk-verlag.html", "r")
html = f.read()
f.close()

it = re.finditer(r"<a .*?href=[\"\'](.*?)[\"\'].*?>(.*?)</a>", html, re.I)
for n, m in enumerate(it):
    print("#{} Name: {}, Link: {}".format(n, m.group(2), m.group(1)))
