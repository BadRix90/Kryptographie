#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.s1 = tkinter.Spinbox(self)
        self.s1["from"] = 0
        self.s1["to"] = 100
        self.s1.pack()
        
        self.s2 = tkinter.Spinbox(self)
        self.s2["values"] = (2,3,5,7,11,13,19)
        self.s2.pack()
        
        self.s3 = tkinter.Spinbox(self)
        self.s3["values"] = ("A", "B", "C")
        self.s3.pack()
        
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
