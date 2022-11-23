#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.cv = tkinter.Canvas(self, width=200, height=100)
        self.cv.pack()
        self.cv.create_oval(10, 10, 190, 90, width=3)
        
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
