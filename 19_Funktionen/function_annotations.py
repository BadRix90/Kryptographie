#!/usr/bin/env python
# -*- coding: utf-8 -*-

def strmult(s: str, n: int) -> str:
    return s*n

def call(f, **kwargs):
    for arg in kwargs:
        if arg not in f.__annotations__:
            raise TypeError("Parameter '{}' unbekannt".format(arg))
        if not isinstance(kwargs[arg], f.__annotations__[arg]):
            raise TypeError("Parameter '{}' hat ungültigen Typ".format(arg))

    ret = f(**kwargs)
    if type(ret) != f.__annotations__["return"]:
        raise TypeError("Ungültiger Rückgabewert")
    return ret

# Gültiger Aufruf mit String s und ganzer Zahl n
print(call(strmult, s="Hallo", n=3))

# Ungültiger Aufruf mit String n
#print(call(strmult, s="Hallo", n="Welt"))

# Ungültiger Aufruf mit ganzer Zahl s
#print(call(strmult, s=13, n=37))
