#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

ip = input("IP-Adresse: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 50000))

try:
    while True:
        nachricht = input("Nachricht: ")
        s.send(nachricht.encode())
finally:
    s.close()
