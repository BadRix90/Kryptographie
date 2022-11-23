#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telnetlib

class POP3Telnet:
    def __init__(self, host, port):
        self.tel = telnetlib.Telnet(host, port)
        self.lese_daten()
        
    def close(self):
        self.tel.close()
        
    def lese_daten(self):
        return self.tel.read_until(b".\r\n", 20.0)
        
    def kommando(self, kom):
        self.tel.write(("{}\r\n".format(kom)).encode())
        return self.lese_daten()

host = "pop.beispiel.de"
port = 110
user = "benutzername"
passwd = "passwort"

pop = POP3Telnet(host, port)
pop.kommando("USER {}".format(user))
pop.kommando("PASS {}".format(passwd))
pop.kommando("LIST")
print(pop.lese_daten().decode())
pop.kommando("QUIT")
pop.close()
