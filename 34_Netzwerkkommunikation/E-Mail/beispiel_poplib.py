#!/usr/bin/env python
# -*- coding: utf-8 -*-

import poplib

pop = poplib.POP3("pop.hostname.de")
pop.user("benutzername")
pop.pass_("passwort")

for i in range(1, pop.stat()[0]+1):
    for zeile in pop.retr(i)[1]:
        print(zeile)
    print("***")
        
pop.quit()
