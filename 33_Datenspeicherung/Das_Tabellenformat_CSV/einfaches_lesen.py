#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

reader = csv.reader(open("beispieldaten_namen.csv"))
for zeile in reader:
    print(zeile)
