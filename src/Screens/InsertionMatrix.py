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

class InsertionMatrix(QWidget):
    def __init__(self, data):
        super().__init__()

        self.dataApp = data

        self.MatrixForm = QFormLayout()
        self.MatrixRowsInput = []

        self.initMatrix()
        self.hideMatrix()

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
        self.layout.addLayout(self.MatrixForm)
        self.setLayout(self.layout)

    def showMatrix(self, text):
        self.hideMatrix()

        for row in range(0, text):
            for col in range(0, text):
                self.dataApp.matrix[row][col] = random.randint(0, 100)
                self.MatrixRowsInput[row][col].setText(str(self.dataApp.matrix[row][col]))
                self.MatrixRowsInput[row][col].setHidden(False)

        self.dataApp.size = text
        print(self.dataApp.matrix)

    def initMatrix(self):

        for column in range(0, 10):
            self.MatrixRowInput = []
            self.MatrixRowLayout = QHBoxLayout()
            for row in range(0, 10):
                self.cellMatrix = QLabel()
                self.cellMatrix.setText("1")
                self.MatrixRowLayout.addWidget(self.cellMatrix)
                self.MatrixRowInput.append(self.cellMatrix)
            self.MatrixForm.addRow(self.MatrixRowLayout)
            self.MatrixRowsInput.append(self.MatrixRowInput)

    def hideMatrix(self):
        for row in self.MatrixRowsInput:
            for col in row:
                col.setHidden(True)
