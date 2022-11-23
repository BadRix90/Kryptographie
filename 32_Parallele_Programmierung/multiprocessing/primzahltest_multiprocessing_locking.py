#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing

class PrimzahlProzess(multiprocessing.Process):
    def __init__(self, zahl, einauslock):
        super().__init__()
        self.Zahl = zahl
        self.EinAusLock = einauslock

    def run(self):
        i = 2
        while i*i <= self.Zahl:
            if self.Zahl % i == 0:
                with self.EinAusLock:
                    print("{} ist nicht prim, "
                          "da {} = {} * {}".format( self.Zahl, 
                                   self.Zahl, i, self.Zahl // i))
                return
            i += 1
        with self.EinAusLock:
            print("{} ist prim".format(self.Zahl))


if __name__ == "__main__":
    meine_prozesse = []
    EinAusLock = multiprocessing.Lock()
    eingabe = input("> ")

    while eingabe != "q":
        try:
            prozess = PrimzahlProzess(int(eingabe), EinAusLock)
            meine_prozesse.append(prozess)
            prozess.start()
        except ValueError:
            with EinAusLock:
                print("Falsche Eingabe!")
        
        with EinAusLock:
            eingabe = input("> ")

    for p in meine_prozesse:
        p.join()
    
