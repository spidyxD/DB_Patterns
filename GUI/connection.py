# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connection.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConnectDB(object):
    def setupUi(self, ConnectDB):
        ConnectDB.setObjectName("ConnectDB")
        ConnectDB.setWindowModality(QtCore.Qt.WindowModal)
        ConnectDB.resize(333, 373)
        ConnectDB.setModal(True)
        self.0 = QtWidgets.QGridLayout(ConnectDB)
        self.0.setObjectName("0")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.message = QtWidgets.QLabel(ConnectDB)
        self.message.setObjectName("message")
        self.gridLayout.addWidget(self.message, 7, 1, 1, 1)
        self.hostLine = QtWidgets.QLineEdit(ConnectDB)
        self.hostLine.setObjectName("hostLine")
        self.gridLayout.addWidget(self.hostLine, 1, 1, 1, 2)
        self.portLine = QtWidgets.QLineEdit(ConnectDB)
        self.portLine.setObjectName("portLine")
        self.gridLayout.addWidget(self.portLine, 2, 1, 1, 2)
        self.connectButton = QtWidgets.QPushButton(ConnectDB)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 7, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.testButton = QtWidgets.QPushButton(ConnectDB)
        self.testButton.setObjectName("testButton")
        self.gridLayout.addWidget(self.testButton, 7, 2, 1, 1)
        self.userLine = QtWidgets.QLineEdit(ConnectDB)
        self.userLine.setObjectName("userLine")
        self.gridLayout.addWidget(self.userLine, 3, 1, 1, 2)
        self.passwordLine = QtWidgets.QLineEdit(ConnectDB)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 4, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(ConnectDB)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(ConnectDB)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.serviceLine = QtWidgets.QLineEdit(ConnectDB)
        self.serviceLine.setObjectName("serviceLine")
        self.gridLayout.addWidget(self.serviceLine, 5, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(ConnectDB)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(ConnectDB)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(ConnectDB)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.0.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(ConnectDB)
        QtCore.QMetaObject.connectSlotsByName(ConnectDB)

    def retranslateUi(self, ConnectDB):
        _translate = QtCore.QCoreApplication.translate
        ConnectDB.setWindowTitle(_translate("ConnectDB", "Connect Settings"))
        self.message.setText(_translate("ConnectDB", "message"))
        self.connectButton.setText(_translate("ConnectDB", "Connect"))
        self.testButton.setText(_translate("ConnectDB", "Test connection"))
        self.label_2.setText(_translate("ConnectDB", "Port"))
        self.label.setText(_translate("ConnectDB", "Host IP"))
        self.label_3.setText(_translate("ConnectDB", "User"))
        self.label_4.setText(_translate("ConnectDB", "Password"))
        self.label_5.setText(_translate("ConnectDB", "Service"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConnectDB = QtWidgets.QDialog()
    ui = Ui_ConnectDB()
    ui.setupUi(ConnectDB)
    ConnectDB.show()
    sys.exit(app.exec_())

