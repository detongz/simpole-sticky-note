#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSlider, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from database import *


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.octSlider = QSlider(Qt.Horizontal, self)
        self.quit = QPushButton(self)
        self.windowUi()
        self.myStyleSheet()

    def windowUi(self):
        self.octSlider.setRange(40, 100)
        self.octSlider.setSingleStep(1)
        self.octSlider.setValue(100)
        self.octSlider.valueChanged.connect(self.changeOpacityValue)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setGeometry(300, 0, 200, 500)
        self.show()
        self.quit.clicked.connect(self.close)  # 关闭窗口

    def changeOpacityValue(self):
        self.setWindowOpacity(self.octSlider.value() * 0.01)

    def myStyleSheet(self):
        self.quit.setStyleSheet(
            'QPushButton{'
            'image:url(close.png); '
            'border:none; max-width:30px;}'
        )  # stylesheet设置样式表 css
        # self.quit.setIcon(QIcon('close.png'))


class tools(QWidget):
    def __init__(self):
        super().__init__()
        self.toolsUi()
        self.btnClose = QPushButton('close', self)

    def toolsUi(self):
        self.btnClose.setStyleSheet()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = window()
    sys.exit(app.exec_())
    # database()
