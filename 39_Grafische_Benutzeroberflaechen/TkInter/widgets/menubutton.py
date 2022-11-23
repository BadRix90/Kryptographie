#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.mb = tkinter.Menubutton(self, text="Hallo Welt")
        
        self.menu = tkinter.Menu(self.mb, tearoff=False)
        self.menu.add_checkbutton(label="Donald Duck")
        self.menu.add_checkbutton(label="Onkel Dagobert")
        self.menu.add_checkbutton(label="Tick, Trick und Track")
        
        self.mb["menu"] = self.menu
        self.mb.pack()
        
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
