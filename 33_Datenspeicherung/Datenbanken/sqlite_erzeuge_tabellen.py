#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("lagerverwaltung.db")
cursor = connection.cursor()


cursor.execute("""CREATE TABLE lager (
    fachnummer INTEGER, seriennummer INTEGER,
    komponente TEXT, lieferant TEXT, reserviert INTEGER
)""")

cursor.execute("""CREATE TABLE lieferanten (
    kurzname TEXT, name TEXT, telefonnummer TEXT
)""")

cursor.execute("""CREATE TABLE kunden (
    kundennummer INTEGER, name TEXT, anschrift TEXT
)""")

