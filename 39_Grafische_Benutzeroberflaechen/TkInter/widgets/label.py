#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.label = tkinter.Label(self)
        self.label["text"] = "Hallo Welt"
        self.label.pack()

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
