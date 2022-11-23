#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xmlrpc.client import ServerProxy, MultiCall

cli = ServerProxy("http://localhost:1337")

mc = MultiCall(cli)
for i in range(10):
    mc.fak(i)
    mc.quad(i)
    
for ergebnis in mc():
    print(ergebnis)
