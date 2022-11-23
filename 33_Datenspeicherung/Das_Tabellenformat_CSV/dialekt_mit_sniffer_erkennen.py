#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

sample = open("beispieldaten_namen.csv").read(1024)
dialect = csv.Sniffer().sniff(sample)
print("Trennzeichen:", dialect.delimiter)
print("Spaltenkoepfe vorhanden:", csv.Sniffer().has_header(sample))

reader = csv.reader(open("beispieldaten_namen.csv"), dialect)
for row in reader:
     print(row)

