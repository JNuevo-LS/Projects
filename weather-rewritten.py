import geocoder
import requests
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QToolTip
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 8))
        update_button = QPushButton(text='Update Weather Data', parent=self)
        self.show()

app = QApplication(sys.argv)                                                            