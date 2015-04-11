# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QWidget(object):
    def setupUi(self, QWidget):
        QWidget.setObjectName("QWidget")
        QWidget.resize(400, 314)
        self.addEvent = QtWidgets.QLineEdit(QWidget)
        self.addEvent.setGeometry(QtCore.QRect(10, 20, 381, 33))
        self.addEvent.setObjectName("addEvent")
        self.addDateTime = QtWidgets.QDateTimeEdit(QWidget)
        self.addDateTime.setGeometry(QtCore.QRect(10, 70, 381, 31))
        self.addDateTime.setObjectName("addDateTime")
        self.addDescription = QtWidgets.QLineEdit(QWidget)
        self.addDescription.setGeometry(QtCore.QRect(10, 120, 381, 141))
        self.addDescription.setObjectName("addDescription")
        self.Submit = QtWidgets.QPushButton(QWidget)
        self.Submit.setGeometry(QtCore.QRect(10, 270, 95, 31))
        self.Submit.setObjectName("Submit")
        self.addDescription.raise_()
        self.addEvent.raise_()
        self.addDateTime.raise_()
        self.Submit.raise_()

        self.retranslateUi(QWidget)
        QtCore.QMetaObject.connectSlotsByName(QWidget)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        QWidget.setWindowTitle(_translate("QWidget", "添加事件"))
        self.addEvent.setPlaceholderText(_translate("QWidget", "添加事件"))
        self.addDescription.setPlaceholderText(_translate("QWidget", "添加详细描述"))
        self.Submit.setText(_translate("QWidget", "提交"))

