#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xmlrpc.client import ServerProxy

cli = ServerProxy("http://localhost:1337")
print(cli.fak(5))
print(cli.quad(5))
