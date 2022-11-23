#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.cv = tkinter.Canvas(self, width=100, height=100)
        self.cv.pack()
        
        punkte = (10, 10,
                  90, 50,
                  10, 90)
        self.cv.create_polygon(*punkte, width=3, fill="orange", outline="black")
        
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
