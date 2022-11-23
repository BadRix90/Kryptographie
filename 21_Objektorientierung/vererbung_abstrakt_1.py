#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        self.X = 1337
        print("Konstruktor von A")
        
    def m(self):
        print("Methode m von A. Es ist self.X =", self.X)
        
        
class B(A):
    def n(self):
        print("Methode n von B")

b = B()
b.n()
b.m()
