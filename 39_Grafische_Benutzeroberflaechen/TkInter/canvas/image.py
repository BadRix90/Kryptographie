#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.cv = tkinter.Canvas(self, width=200, height=200)
        self.cv.pack()
        
        self.img = tkinter.PhotoImage(file="lena.png")
        self.cv.create_image(0, 0, image=self.img, anchor="nw")

        
root = tkinter.Tk()
app = MyApp(root)
app.mainloop()
