#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.names = ("Donald Duck", "Dagobert Duck", "Gustav Gans")
        
        self.group = tkinter.LabelFrame(self)
        self.group["text"] = "Entenhausen"
        self.group.pack()
        
        self.checks = []
        self.vars = []
        
        for name in self.names:
            var = tkinter.BooleanVar()
            var.set(False)
            
            check = tkinter.Checkbutton(self.group)
            check["text"] = name
            check["command"] = self.handler
            check["variable"] = var
            check.pack(anchor="w")
            
            self.checks.append(check)
            self.vars.append(var)
        
    def handler(self):
        print(" und ".join([name for name, var in zip(self.names, self.vars) if var.get()]))

root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
