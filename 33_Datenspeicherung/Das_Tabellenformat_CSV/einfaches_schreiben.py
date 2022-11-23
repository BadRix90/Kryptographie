#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

writer = csv.writer(open("beispieldaten_autos.csv", "w"))
writer.writerow(["marke", "modell", "leistung_in_ps"])
daten = (
    ["Volvo", "P245", "130"], ["Ford", "Focus", "90"],
    ["Mercedes", "CLK", "250"], ["Audi", "A6", "350"],
    )
writer.writerows(daten)
