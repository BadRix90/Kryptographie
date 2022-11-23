#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import cProfile

def calc1(n):
    return n**2
    
def calc2(n):
    return math.sqrt(n)
    
def calc3(n):
    return math.log(n+1)
    
def programm():
    for i in range(100):
        calc1(i)
        for j in range(100):
            calc2(j)
            for k in range(100):
                calc3(k)

cProfile.run("programm()")
