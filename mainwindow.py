import sys
from add import *
from window import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from database import *


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = addWindow()
        self.mw = Ui_MainWindow()
        self.mw.setupUi(self)
        self.mw.add.clicked.connect(self.on_add_clicked)
        # self.w.adw.Submit.clicked.connect(self.add_item)
        self.connect(self.w.adw.Submit.clicked,Sig)
        self.count = self.mw.tableWidget.rowCount()
        print(self.count)

    def on_add_clicked(self):
        self.w.show()

    def add_item(self):
        self.count += 1
        # self.mw.tableWidget.insertRow(self.count)
        self.mw.tableWidget.setRowCount(self.count)
        item = [self.w.adw.addEvent.text(), self.w.adw.addDateTime.text(), self.w.adw.addDescription.text()]
        for i in range(3):
            self.mw.tableWidget.setItem(self.count - 1, i, QTableWidgetItem(item[i]))
        print(self.count)
        # self.w.deleteLater()
        # self.w = addWindow()


class addWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.adw = Ui_QWidget()
        self.adw.setupUi(self)
        self.adw.Submit.clicked.connect(self.submit_clicked)

    def submit_clicked(self):
        self.close()