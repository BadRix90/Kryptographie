#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        self.X = 1337
        print("Konstruktor von A")
        
    def m(self):
        print("Methode m von A. Es ist self.X =", self.X)
        
        
class B(A):
    def __init__(self):
        self.Y = 10000
        print("Konstruktor von B")
        
    def n(self):
        print("Methode n von B. Es ist self.Y =", self.Y)


b = B()
b.n()
#b.m() # <--- Fehler, da b kein Attribut X besitzt
