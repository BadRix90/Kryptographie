#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.sax as sax

class DictHandler(sax.handler.ContentHandler):
    typen = {
        "int" : int,
        "str" : str
        }    
        
    def __init__(self):
        self.ergebnis = {}
        self.schluessel = ""
        self.wert = ""
        self.aktiv = None
        self.typ = None

        
    def startElement(self, name, attrs):
        if name == "eintrag":
            self.schluessel = ""
            self.wert = ""
        elif name in ("schluessel", "wert"):
            self.aktiv = name
            try:
                self.typ = self.typen[attrs["typ"]]
            except KeyError:
                self.typ = str
            
    def endElement(self, name):
        if name == "eintrag":
            self.ergebnis[self.schluessel] = self.typ(self.wert)
        elif name in ("schluessel", "wert"):
            self.aktiv = None
            
    def characters(self, content):
        if self.aktiv == "schluessel":
            self.schluessel += content
        elif self.aktiv == "wert":
            self.wert += content

def lade_dict(dateiname):
    handler = DictHandler()
    parser = sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(dateiname)
    return handler.ergebnis

print(lade_dict("dict.xml"))