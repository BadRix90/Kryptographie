# -*- coding: utf-8 -*-

import PersonInterface

class Person(PersonInterface):
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
        
    def getName(self):
        return self.vorname + " " + self.nachname