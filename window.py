# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 443)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(10, 380, 95, 31))
        self.add.setObjectName("add")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 381, 361))
        # self.tableWidget.setStyleSheet("selection-background-color:lightblue;")
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 27))
        self.menubar.setObjectName("menubar")
        self.option = QtWidgets.QMenu(self.menubar)
        self.option.setObjectName("option")
        MainWindow.setMenuBar(self.menubar)
        self.deleteSelected = QtWidgets.QAction(MainWindow)
        self.deleteSelected.setObjectName("deleteSelected")
        self.clear = QtWidgets.QAction(MainWindow)
        self.clear.setObjectName("clear")
        self.option.addAction(self.deleteSelected)
        self.option.addAction(self.clear)
        self.menubar.addAction(self.option.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add.setText(_translate("MainWindow", "添加事件"))
        self.tableWidget.setSortingEnabled(False)
        self.option.setTitle(_translate("MainWindow", "选项"))
        self.deleteSelected.setText(_translate("MainWindow", "删除所选项"))
        self.clear.setText(_translate("MainWindow", "清空所有事件"))
        self.tableWidget.setItem(0, 0, QTableWidgetItem('hello'))
        self.tableWidget.setHorizontalHeaderLabels(('事件', '时间', '事件描述'))