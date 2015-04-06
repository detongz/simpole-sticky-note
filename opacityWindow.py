#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QSlider, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt, QObject


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.windowUi()
        self.toolboxUi()
        self.myStyleSheet()

    def windowUi(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setGeometry(300, 0, 200, 500)
        self.show()

    def toolboxUi(self):
        self.quit = QPushButton()
        self.octSlider = QSlider(Qt.Horizontal)
        self.octSlider.setRange(40, 100)
        self.octSlider.setSingleStep(1)
        self.octSlider.setValue(100)
        self.octSlider.valueChanged.connect(self.changeOpacityValue)
        self.quit.clicked.connect(self.close)  # 关闭窗口

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.quit)
        hbox.addWidget(self.octSlider)

        self.vbox = QVBoxLayout()
        self.vbox.addStretch(1)
        self.vbox.addLayout(hbox)

        # self.setLayout(self.vbox)
        # self.show()

    def changeOpacityValue(self):
        self.setWindowOpacity(self.octSlider.value() * 0.01)

    def myStyleSheet(self):
        self.quit.setStyleSheet(
            'QPushButton{'
            'image:url(close.png); '
            'border:none; max-width:30px;}'
        )  # stylesheet设置样式表 css
        # self.quit.setIcon(QIcon('close.png'))

    def mouseMoveEvent(self, QMouseEvent):
        self.setMouseTracking(1)
        self.setLayout(self.vbox)