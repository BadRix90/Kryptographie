#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import tkinter.scrolledtext

class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.text = tkinter.scrolledtext.ScrolledText(master)
        self.text.pack()
        self.text.insert("end", "Hallo Welt\n")
        
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
