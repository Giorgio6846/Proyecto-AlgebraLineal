from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
    QHBoxLayout,
    QPushButton,
    QInputDialog,
    QFormLayout)

from PySide6.QtGui import QFont
from PySide6.QtCore import *
import random
from Screens import viewMatrix

class InsertionMatrix(QWidget):
    def __init__(self, data):
        super().__init__()

        self.dataApp = data
        self.matrixWidget = viewMatrix.matrixShow()

        self.TitleScreen = QLabel("Ingreso de matriz")
        self.TitleScreen.setFont(QFont("Arial", 24))
        self.TitleScreen.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.TitleScreen.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.TitleScreen.setFixedHeight(30)

        self.SizeData = QInputDialog()
        self.SizeData.setLabelText("Ingrese el tamaño de la matriz entre 4 a 10")
        self.SizeData.setInputMode(QInputDialog.IntInput)
        self.SizeData.setIntRange(4, 10)
        self.SizeData.setOption(QInputDialog.NoButtons, True)

        self.SizeData.intValueChanged.connect(self.showMatrix)

        self.LayoutSize = QHBoxLayout()
        self.LayoutSize.addWidget(self.SizeData)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.TitleScreen)
        self.layout.addLayout(self.LayoutSize)
        self.layout.addLayout(self.matrixWidget.viewMatrix)
        self.setLayout(self.layout)

    def showMatrix(self, text):
        self.dataApp.size = text

        for row in range(0, self.dataApp.size):
            for col in range(0, self.dataApp.size):
                self.dataApp.initMatrix[row][col] = random.randint(0, 100)

        self.matrixWidget.sizeMatrix = self.dataApp.size
        self.matrixWidget.matrix = self.dataApp.initMatrix
        
        self.matrixWidget.showMatrixInt()
