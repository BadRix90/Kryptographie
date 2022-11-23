#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class MeinWidget(QtWidgets.QWidget):
    def __init__(self, parent=None): 
        super().__init__(parent) 
        self.font = QtGui.QFont("Helvetica", 16) 
        self.pen = QtGui.QPen(QtGui.QColor(0,0,255))
        
    def paintEvent(self, event): 
        painter = QtGui.QPainter(self) 
        painter.setPen(self.pen) 
        painter.setFont(self.font) 
        painter.drawText(self.rect(), QtCore.Qt.AlignCenter, "Hallo Welt")
        
app = QtWidgets.QApplication(sys.argv) 
widget = MeinWidget()
widget.resize(150, 150) 
widget.show()
sys.exit(app.exec_())
 
