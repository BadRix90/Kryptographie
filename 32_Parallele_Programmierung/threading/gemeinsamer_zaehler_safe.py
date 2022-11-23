#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

class MeinThread(threading.Thread):
    lock = threading.Lock()
    zaehler = 0
    def run(self):
        for i in range(2000000):
            with MeinThread.lock:
                MeinThread.zaehler += 1


t1 = MeinThread()
t2 = MeinThread()
t1.start(), t2.start()
t1.join(), t2.join()

print(MeinThread.zaehler)
