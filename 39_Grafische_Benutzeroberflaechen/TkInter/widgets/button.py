#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.ok = tkinter.Button(self)
        self.ok["text"] = "Beschriftung"
        self.ok["command"] = self.handler
        self.ok.pack()
        
    def handler(self):
        print("Button gedrückt")

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
