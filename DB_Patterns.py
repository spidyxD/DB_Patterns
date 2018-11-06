# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Patterns.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox
import os, sys
import connection as window_conect
import analisis as analisis
import pandas as pd
from pandas import ExcelWriter
import matplotlib.pyplot as plt
import PIL
from PIL import Image

class Ui_MainWindow(object):
    flag = False
    #Main functions
    def userGraphic(self):
       fig = plt.figure()
       ax = analisis.userGraphic()
       plt.title('Users Graphic')
       fig.savefig('Graphics/user.png')
       pixmap = QtGui.QPixmap('Graphics/user.png')
       pixmap.scaled(self.userLabel.geometry().width(),self.userLabel.geometry().height(),QtCore.Qt.KeepAspectRatio)
       self.userLabel.setPixmap(pixmap)
       self.userLabel.setScaledContents(True)
        
    def tableGraphic(self):
       fig = plt.figure()
       ax = analisis.tableGraphic()
       plt.title('Table Graphic')
       fig.savefig('Graphics/table.png')
       pixmap = QtGui.QPixmap('Graphics/table.png')
       pixmap.scaled(self.tbLabel.geometry().width(),self.tbLabel.geometry().height(),QtCore.Qt.IgnoreAspectRatio)
       self.tbLabel.setPixmap(pixmap)   
       self.tbLabel.setScaledContents(True)

    def tablespaceGraphic(self):
        fig = plt.figure()
        ax = analisis.tablespaceGraphic()
        plt.title('Tablespace Graphic')
        fig.savefig('Graphics/tbs.png')
        pixmap = QtGui.QPixmap('Graphics/tbs.png')
        pixmap.scaled(self.tbsLabel.geometry().width(),self.tbsLabel.geometry().height(),QtCore.Qt.IgnoreAspectRatio)
        self.tbsLabel.setPixmap(pixmap)  
        self.tbsLabel.setScaledContents(True)
    
    def segOwnerGraphic(self):
        fig = plt.figure()
        ax = analisis.segOwnerGraphic()
        plt.title('Segment owner Graphic')
        fig.savefig('Graphics/segOw.png')
        pixmap = QtGui.QPixmap('Graphics/segOw.png')
        pixmap.scaled(self.segLabel.geometry().width(),self.segLabel.geometry().height(),QtCore.Qt.KeepAspectRatio)
        self.segLabel.setPixmap(pixmap)  
        self.segLabel.setScaledContents(True)

    def operationGraphic(self):
        fig = plt.figure()
        ax = analisis.operationGraphic()
        plt.title('Operation Graphic')
        fig.savefig('Graphics/operation.png')
        pixmap = QtGui.QPixmap('Graphics/operation.png')
        pixmap.scaled(self.opLabel.geometry().width(),self.opLabel.geometry().height(),QtCore.Qt.IgnoreAspectRatio)
        self.opLabel.setPixmap(pixmap)
        self.opLabel.setScaledContents(True)

    def dateGraphic(self):
        fig = plt.figure()
        ax = analisis.dateGraphic()
        plt.title('Date Graphic')
        ax.legend()
        fig.savefig('Graphics/date.png')
        pixmap = QtGui.QPixmap('Graphics/date.png')
        pixmap.scaled(self.dateLabel.geometry().width(),self.dateLabel.geometry().height(),QtCore.Qt.IgnoreAspectRatio)
        self.dateLabel.setPixmap(pixmap)
        self.dateLabel.setScaledContents(True)

    def timeGraphic(self):
        fig = plt.figure()
        ax = analisis.timeGraphic()
        plt.title('Date Graphic')
        fig.savefig('Graphics/time.png')
        pixmap = QtGui.QPixmap('Graphics/time.png')
        pixmap.scaled(self.timeLabel.geometry().width(),self.timeLabel.geometry().height(),QtCore.Qt.IgnoreAspectRatio)
        self.timeLabel.setPixmap(pixmap)    
        self.timeLabel.setScaledContents(True)
    
    def formatTable(self):
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item1 = QtWidgets.QTableWidgetItem()
        item1.setText("USERNAME")
        item1.setFont(font)
        item2 = QtWidgets.QTableWidgetItem()
        item2.setText("TABLESPACE")
        item2.setFont(font)
        item3 = QtWidgets.QTableWidgetItem()
        item3.setText("TABLE")
        item3.setFont(font)
        item4 = QtWidgets.QTableWidgetItem()
        item4.setText("SEG_OWNER")
        item4.setFont(font)
        item5 = QtWidgets.QTableWidgetItem()
        item5.setText("OPERATION")
        item5.setFont(font)
        item6 = QtWidgets.QTableWidgetItem()
        item6.setText("SQL")
        item6.setFont(font)
        item7 = QtWidgets.QTableWidgetItem()
        item7.setText("SQL-1")
        item7.setFont(font)
        item8 = QtWidgets.QTableWidgetItem()
        item8.setText("DATE")
        item8.setFont(font)
        item9 = QtWidgets.QTableWidgetItem()
        item9.setText("TIME")
        item9.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item1)
        self.tableWidget.setHorizontalHeaderItem(1, item2)
        self.tableWidget.setHorizontalHeaderItem(2, item3)
        self.tableWidget.setHorizontalHeaderItem(3, item4)
        self.tableWidget.setHorizontalHeaderItem(4, item5)
        self.tableWidget.setHorizontalHeaderItem(5, item6)
        self.tableWidget.setHorizontalHeaderItem(6, item7)
        self.tableWidget.setHorizontalHeaderItem(7, item8)
        self.tableWidget.setHorizontalHeaderItem(8, item9)

    def loadTable(self):
        self.flag = True
        self.userGraphic()
        self.tablespaceGraphic()
        self.tableGraphic()
        self.segOwnerGraphic()
        self.dateGraphic()
        self.operationGraphic()
        self.timeGraphic()
        self.tableWidget.setRowCount(0)
        data = analisis.loadTable() 
        if  len(data)>0:
            self.tableWidget.clear()
            self.formatTable()
            df = data[['USERNAME','TABLE_SPACE', 'TABLE_NAME', 'SEG_OWNER', 'OPERATION', 'SQL_', 'SQL_1', 'DATE_', 'TIME_']].values
            for row_number, row_data in enumerate (df):
                self.tableWidget.insertRow(row_number)
                for col_number, a in enumerate (row_data):   
                    self.tableWidget.setItem(row_number,col_number,QtWidgets.QTableWidgetItem(str(a)))
        else:
            msg = QMessageBox(self.centralwidget)
            msg.setText("NO DATA REGISTER INTO DB LOGFILES")
            msg.setInformativeText("DATA NOT FOUND! , please change the logfiles selected")
            msg.setWindowTitle("Warning!")
            msg.exec_()  
    
    def filterGeneral(self):
        print('gen')
        return analisis.loadTable()
        

    def filterUser(self):
        text = self.filter.text()
        text = text.upper() 
        print('user')
        return analisis.filterUser(text)


    def filterTable(self):
        text = self.filter.text()
        text = text.upper() 
        print('tb')
        return analisis.filterTable(text)

    def filterTBS(self):
        text = self.filter.text()
        text = text.upper() 
        print('tbs')
        return analisis.filterTableSpace(text)

    def filterSEGOW(self):
        text = self.filter.text()
        text = text.upper() 
        print('segow')
        return analisis.filterSegOw(text) 

    def filterOP(self):
        text = self.filter.text()
        text = text.upper()
        print('op')
        return analisis.filterOperation(text) 

    def filterDate(self):
        text = self.filter.text()
        text = text.upper()
        print('date')
        return analisis.filterDate(text)  

    def filterTime(self):
        text = self.filter.text()
        text = text.upper()
        print('time') 
        return analisis.filterTime(text)   
    
    def switcherFilters(self,x):
        if x == 'GENERAL':
            return self.filterGeneral()
        elif x == 'USER_NAME':
            return self.filterUser()
        elif x == 'TABLE_NAME':    
            return self.filterTable()
        elif x == 'TABLESPACE_NAME':  
            return self.filterTBS()
        elif x == 'SEG_OWNER':
            return self.filterSEGOW()
        elif x == 'OPERATION':
            return self.filterOP()
        elif x == 'DATE': 
            return self.filterDate()
        elif x == 'TIME':
            return self.filterTime()
        else:
            return self.filterGeneral()  
          
    def loadFilters(self):
        text = self.filter.text()
        print(self.chooser.currentText())
        data = self.switcherFilters(self.chooser.currentText()) 
        if self.chooser.currentText() == 'GENERAL':
           self.loadTable()
           return 0    
        elif len(text) > 0 and len(data) > 0:
            self.tableWidget.clear()
            self.formatTable()
            df = data[['USERNAME','TABLE_SPACE', 'TABLE_NAME', 'SEG_OWNER', 'OPERATION', 'SQL_', 'SQL_1', 'DATE_', 'TIME_']].values    
            for row_number, row_data in enumerate (df):
                self.tableWidget.insertRow(row_number)
                for col_number, a in enumerate (row_data):  
                    self.tableWidget.setItem(row_number,col_number,QtWidgets.QTableWidgetItem(str(a)))       
        else:
            msg = QMessageBox(self.centralwidget)
            msg.setText("DATA NOT REGISTER INTO DB LOGFILES")
            msg.setInformativeText("Data not found, please enter a valid data")
            msg.setWindowTitle("Warning!")
            msg.exec_()  

     #-- Tools --
    def Undo(self):
       self.filter.undo()

    def Delete(self):
       self.filter.clear()

    def Redo(self):
       self.filter.redo()
 
    def Cut(self):
       self.filter.cut()
 
    def Copy(self):
       self.filter.copy()
 
    def Paste(self):
       self.filter.paste()
    
    def delete(self):
        self.filter.setText('')

    def about(self):            
         msg = QMessageBox(self.centralwidget)
         msg.setText("Welcome to DB_Patterns")
         msg.setInformativeText("This is an educational project created by Roger Amador and Adrian Prendas \n Powered by Oracle")
         msg.setWindowTitle("DB_Patterns")
         msg.exec_() 
    
    def connectDB(self):            
        return 0


    def saveData(self):
        if self.chooser.currentText() == 'GENERAL':
           data = analisis.loadTable() 
        else:
           data = self.switcherFilters(self.chooser.currentText()) 
        if data.empty == False and self.flag==True:
            path = QFileDialog.getSaveFileName(self.menuFile, 'Save As', os.getenv('HOME'), 'Libro Excel(*.xlsx)') 
            if  path != ('', ''):    
                try:
                    writer = ExcelWriter(path[0])
                    data.to_excel(writer,'Historial de registros',index=False)
                    print(path)
                    writer.save()
                except Exception as error:
                    self.flag = False
                    raise Exception("There was an error saving the file: ".format(error))
            else: 
                #QFileDialog.destroy()
                return None       
        else:
            self.flag = False
            msg = QMessageBox(self.centralwidget)
            msg.setText("You cannot save an empty table")
            msg.setInformativeText("Please generate some data before saving")
            msg.setWindowTitle("Warning!")
            msg.exec_() 


    def exitApp(self):
        sys.exit()    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 585)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.search = QtWidgets.QPushButton(self.groupBox)
        self.search.setObjectName("search")
        self.search.clicked.connect(self.loadFilters)
        self.gridLayout_2.addWidget(self.search, 0, 2, 1, 1)
        self.chooser = QtWidgets.QComboBox(self.groupBox)
        self.chooser.setObjectName("chooser")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.chooser.addItem("")
        self.gridLayout_2.addWidget(self.chooser, 0, 1, 1, 1)
        self.filter = QtWidgets.QLineEdit(self.groupBox)
        self.filter.setObjectName("filter")
        self.gridLayout_2.addWidget(self.filter, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 2, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 3, 1, 1)
        self.loadButton = QtWidgets.QPushButton(self.groupBox)
        self.loadButton.setObjectName("loadButton")
        self.loadButton.clicked.connect(self.loadTable)
        self.gridLayout_2.addWidget(self.loadButton, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 4, 1, 1)
        self.graphics = QtWidgets.QTabWidget(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.graphics.setFont(font)
        self.graphics.setAutoFillBackground(False)
        self.graphics.setObjectName("graphics")
        self.tab_user = QtWidgets.QWidget()
        self.tab_user.setObjectName("tab_user")
        self.userLabel = QtWidgets.QLabel(self.tab_user)
        self.userLabel.setGeometry(QtCore.QRect(-4, 2, 461, 381))
        self.userLabel.setText("")
        self.userLabel.setObjectName("userLabel")
        self.graphics.addTab(self.tab_user, "")
        self.tab_tbs_name = QtWidgets.QWidget()
        self.tab_tbs_name.setObjectName("tab_tbs_name")
        self.tbsWidget = QtWidgets.QWidget(self.tab_tbs_name)
        self.tbsWidget.setGeometry(QtCore.QRect(-1, -1, 461, 381))
        self.tbsWidget.setObjectName("tbsWidget")
        self.tbsLabel = QtWidgets.QLabel(self.tbsWidget)
        self.tbsLabel.setGeometry(QtCore.QRect(0, 10, 461, 381))
        self.tbsLabel.setText("")
        self.tbsLabel.setObjectName("tbsLabel")
        self.graphics.addTab(self.tab_tbs_name, "")
        self.tab_tb_name = QtWidgets.QWidget()
        self.tab_tb_name.setObjectName("tab_tb_name")
        self.tableWidget_2 = QtWidgets.QWidget(self.tab_tb_name)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tbLabel = QtWidgets.QLabel(self.tableWidget_2)
        self.tbLabel.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.tbLabel.setText("")
        self.tbLabel.setObjectName("tbLabel")
        self.graphics.addTab(self.tab_tb_name, "")
        self.tab_owner = QtWidgets.QWidget()
        self.tab_owner.setObjectName("tab_owner")
        self.ownerWidget = QtWidgets.QWidget(self.tab_owner)
        self.ownerWidget.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.ownerWidget.setObjectName("ownerWidget")
        self.segLabel = QtWidgets.QLabel(self.ownerWidget)
        self.segLabel.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.segLabel.setText("")
        self.segLabel.setObjectName("segLabel")
        self.graphics.addTab(self.tab_owner, "")
        self.tab_operation = QtWidgets.QWidget()
        self.tab_operation.setObjectName("tab_operation")
        self.operationWidget = QtWidgets.QWidget(self.tab_operation)
        self.operationWidget.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.operationWidget.setObjectName("operationWidget")
        self.opLabel = QtWidgets.QLabel(self.operationWidget)
        self.opLabel.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.opLabel.setText("")
        self.opLabel.setObjectName("opLabel")
        self.graphics.addTab(self.tab_operation, "")
        self.tab_date = QtWidgets.QWidget()
        self.tab_date.setObjectName("tab_date")
        self.dateWidget = QtWidgets.QWidget(self.tab_date)
        self.dateWidget.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.dateWidget.setObjectName("dateWidget")
        self.dateLabel = QtWidgets.QLabel(self.dateWidget)
        self.dateLabel.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.dateLabel.setText("")
        self.dateLabel.setObjectName("dateLabel")
        self.graphics.addTab(self.tab_date, "")
        self.tab_time = QtWidgets.QWidget()
        self.tab_time.setObjectName("tab_time")
        self.timeWidget = QtWidgets.QWidget(self.tab_time)
        self.timeWidget.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.timeWidget.setObjectName("timeWidget")
        self.timeLabel = QtWidgets.QLabel(self.timeWidget)
        self.timeLabel.setGeometry(QtCore.QRect(0, 0, 461, 381))
        self.timeLabel.setText("")
        self.timeLabel.setObjectName("timeLabel")
        self.graphics.addTab(self.tab_time, "")
        self.gridLayout_2.addWidget(self.graphics, 1, 3, 1, 3)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 2, 3)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1088, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExport.setShortcut("Ctrl+S")
        self.actionExport.triggered.connect(self.saveData)
        

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Ctrl+E")
        self.actionExit.triggered.connect(self.exitApp)

        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCopy.setShortcut("Ctrl+C")
        self.actionCopy.triggered.connect(self.Copy)

        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPaste.setShortcut("Ctrl+P")
        self.actionPaste.triggered.connect(self.Paste)

        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete.setShortcut("Ctrl+Supr")
        self.actionDelete.triggered.connect(self.Delete)

        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionRedo.setShortcut("Ctrl+Y")
        self.actionRedo.triggered.connect(self.Redo)

        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUndo.setShortcut("Ctrl+Z")
        self.actionUndo.triggered.connect(self.Undo)

        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionConnect.setShortcut("Ctrl+Q")
        self.actionConnect.triggered.connect(self.connectDB)

      
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.about)

        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCut.setShortcut("Ctrl+X")
        self.actionCut.triggered.connect(self.Cut)

        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionUndo)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.graphics.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DB_Patterns"))
        self.groupBox.setTitle(_translate("MainWindow", "DBPatterns"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.chooser.setItemText(0, _translate("MainWindow", "GENERAL"))
        self.chooser.setItemText(1, _translate("MainWindow", "USER_NAME"))
        self.chooser.setItemText(2, _translate("MainWindow", "TABLESPACE_NAME"))
        self.chooser.setItemText(3, _translate("MainWindow", "TABLE_NAME"))
        self.chooser.setItemText(4, _translate("MainWindow", "SEG_OWNER"))
        self.chooser.setItemText(5, _translate("MainWindow", "OPERATION"))
        self.chooser.setItemText(6, _translate("MainWindow", "DATE"))
        self.chooser.setItemText(7, _translate("MainWindow", "TIME"))
        self.label.setText(_translate("MainWindow", "    Graphics"))
        self.loadButton.setText(_translate("MainWindow", "Load data"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_user), _translate("MainWindow", "USER"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_tbs_name), _translate("MainWindow", "TABLESPACE"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_tb_name), _translate("MainWindow", "TABLE"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_owner), _translate("MainWindow", "SEG_OWNER"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_operation), _translate("MainWindow", "OPERATION"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_date), _translate("MainWindow", "DATE"))
        self.graphics.setTabText(self.graphics.indexOf(self.tab_time), _translate("MainWindow", "TIME"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "USERNAME"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TABLESPACE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TABLE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SEG_OWNER"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "OPERATION"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "SQL"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "SQL-1"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "TIME"))
        self.menuFile.setTitle(_translate("MainWindow", "Init"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExport.setText(_translate("MainWindow", " Export data"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionConnect.setText(_translate("MainWindow", "Connect to DB"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

