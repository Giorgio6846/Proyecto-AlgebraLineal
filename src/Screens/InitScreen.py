from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy, QHBoxLayout, QPushButton
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtCore import *

class InitScreen(QWidget):

    def __init__(self):
        super().__init__()  
        
        
        self.TitleScreen = QLabel("Proyecto Algebra Lineal")
        self.TitleScreen.setFont(QFont("Arial", 24))
        self.TitleScreen.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.TitleScreen.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.TitleScreen.setFixedHeight(30)

        self.Integrantes = QLabel(
            """INTEGRANTES \nFabio Osorio Ramos              202211499 \nGiorgio Mancusi Barreda       202216613\nMathias Hualtibamba Valerio 202214421 \n"""
        )
        self.Integrantes.setFont(QFont("Arial", 24))
        self.Integrantes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.TitleScreen)
        self.layout.addWidget(self.Integrantes)
        self.setLayout(self.layout)
        