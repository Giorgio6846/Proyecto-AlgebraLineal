from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtCore import *

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class InitScreen(QWidget):

    def __init__(self, index):
        super().__init__()  
        self.setWindowTitle('test')

        
        self.TitleScreen = QLabel("Proyecto Algebra Lineal")
        self.TitleScreen.setFont(QFont("Arial", 24))
        self.TitleScreen.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.TitleScreen)
        self.layout.addWidget(Color('Red'))
        self.setLayout(self.layout)