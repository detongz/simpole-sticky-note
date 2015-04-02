#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSlider, QPushButton
from PyQt5.QtCore import Qt


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.octSlider = QSlider(Qt.Horizontal, self)
        self.quit = QPushButton("x", self)
        self.initUi()

    def initUi(self):

        self.octSlider.setRange(40, 100)
        self.octSlider.setSingleStep(1)
        self.octSlider.setValue(100)
        self.octSlider.valueChanged.connect(self.changeOpacityValue)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setGeometry(300, 0, 200, 500)
        self.show()

    def changeOpacityValue(self):
        self.setWindowOpacity(self.octSlider.value()*0.01)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = window()
    sys.exit(app.exec_())
