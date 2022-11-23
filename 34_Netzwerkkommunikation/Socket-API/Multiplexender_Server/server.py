#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import selectors

def message(selector, client):
    nachricht = client.recv(1024)
    ip = client.getpeername()[0]
    if nachricht:
        print("[{}] {}".format(ip, nachricht.decode()))
    else:
        print("+++ Verbindung zu {} beendet".format(ip))
        selector.unregister(client)
        client.close()

def accept(selector, sock):
    connection, addr = sock.accept()
    connection.setblocking(False)
    selector.register(connection, selectors.EVENT_READ, message)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 50000))
server.setblocking(False)
server.listen(1)

selector = selectors.DefaultSelector()
selector.register(server, selectors.EVENT_READ, accept)

while True:
    for key, mask in selector.select():
        key.data(selector, key.fileobj)
