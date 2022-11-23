#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gettext
import random 

trans = gettext.translation("meinprogramm", "locale", ["de"])
trans.install()

werte = []

while True:
    w = input(_("Please enter a value: "))
    if not w:
        break
        
    werte.append(w)
    
print(_("The random choice is {}").format(random.choice(werte)))
