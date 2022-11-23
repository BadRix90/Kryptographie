#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent import futures
from time import sleep, time

def test(t):
    sleep(t)
    print("Ich habe {} Sekunden gewartet. Zeit: {:.0f}".format(t, time()))
    
e = futures.ThreadPoolExecutor(max_workers=3)
print("Startzeit:                          {:.0f}".format(time()))
e.submit(test, 9)
e.submit(test, 2)
e.submit(test, 5)
e.submit(test, 6)
print("Alle Aufgaben gestartet.")
e.shutdown()
print("Alle Aufgaben erledigt.")
