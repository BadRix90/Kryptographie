#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
import sys
import modell
import view

m = modell.Modell("adressbuch.txt")
app = QtWidgets.QApplication(sys.argv) 
liste = view.View(m) 
liste.resize(200, 500) 
liste.show()
sys.exit(app.exec_())
