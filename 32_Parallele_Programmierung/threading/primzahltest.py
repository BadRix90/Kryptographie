#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

class PrimzahlThread(threading.Thread):
    def __init__(self, zahl):
        super().__init__()
        self.Zahl = zahl

    def run(self):
        i = 2
        while i*i <= self.Zahl:
            if self.Zahl % i == 0:
                print("{} ist nicht prim, "
                      "da {} = {} * {}".format( self.Zahl, 
                                   self.Zahl, i, self.Zahl // i))
                return
            i += 1
        print("{} ist prim".format(self.Zahl))


meine_threads = []
eingabe = input("> ")

while eingabe != "q":
    try:
        thread = PrimzahlThread(int(eingabe))
        meine_threads.append(thread)
        thread.start()
    except ValueError:
        print("Falsche Eingabe!")
    eingabe = input("> ")

for t in meine_threads:
    t.join()
 
