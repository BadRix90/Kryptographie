#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

regexp = {
        "Name" : r"([A-Za-z]+)\s([A-Za-z]+)",
        "Adr" : r"([A-Za-z]+)\s(\d+)\s*(\d{5})\s([A-Za-z]+)",
        "Tel" : r"(\+\d{2})\s(\d{4})\s(\d{3,})"
        }

def leseDatei(datei):
    d = {}
    
    f = open(datei)
    for zeile in f:
        if ":" in zeile:
            key, d[key] = (s.strip() for s in zeile.split(":",1))
        elif "key" in locals():
            d[key] += "\n{}".format(zeile.strip())
    f.close()
    
    return d

def analysiereDaten(daten, regexp):
    for key in daten:
        if key not in regexp:
            return False
            
        m = re.match(regexp[key], daten[key])
        if not m:
            return False
        daten[key] = m.groups()
        
    return True

daten = leseDatei("id.txt")
if analysiereDaten(daten, regexp):
    print(daten)
else:
    print("Die Angaben sind fehlerhaft")
