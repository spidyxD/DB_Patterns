from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox
import os, sys

class ChildWindow(object):
    def __init__(self, name=None):
        super(ChildWindow, self).__init__()
        self.name = name
        self.initUI()
 
    def initUI(self):
        btn1 = QtGui.QPushButton("%s" % self.name, self)
        btn1.move(30, 50)
 
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Child Window %s' % self.name)
        self.show()
 
 
class MainWindow(object):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.children = []
        self.initUI()
        
    def initUI(self):
        btn1 = QtGui.QPushButton("Start", self)
        btn1.move(30, 50)
 
        self.le = QtGui.QLineEdit(self)
        self.le.move(30, 20)
      
        btn1.clicked.connect(self.buttonClicked)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Multiple windows example')
        self.show()
        
    def buttonClicked(self):
        child = ChildWindow(name=self.le.text())
        self.children.append(child)
 

   
 
 
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

  