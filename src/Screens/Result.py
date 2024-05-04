from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QStackedLayout)

from PySide6.QtGui import QFont
from PySide6.QtCore import *
from enum import Enum
from Screens import viewMatrix


MatrixOptions = Enum("MatrixOptions", ["Original", "P", "L", "U"])

class Result(QWidget):

    def __init__(self, data):
        super().__init__()
        self.dataApp = data

        self.OriginalMatrix = viewMatrix.matrixShow()
        self.PMatrix = viewMatrix.matrixShow()
        self.LMatrix = viewMatrix.matrixShow()
        self.UMatrix = viewMatrix.matrixShow()

        self.matrixOptionsLayout = QHBoxLayout()
        self.buttonOriginalMatrix = QPushButton(text = "Original")
        self.buttonPMatrix = QPushButton(text = "P")
        self.buttonLMatrix = QPushButton(text = "L")
        self.buttonUMatrix = QPushButton(text = "U")

        self.matrixOptionsLayout.addWidget(self.buttonOriginalMatrix)
        self.matrixOptionsLayout.addWidget(self.buttonPMatrix)
        self.matrixOptionsLayout.addWidget(self.buttonLMatrix)
        self.matrixOptionsLayout.addWidget(self.buttonUMatrix)

        self.buttonOriginalMatrix.clicked.connect(lambda: self.setMethodIndex(MatrixOptions.Original))
        self.buttonPMatrix.clicked.connect(lambda: self.setMethodIndex(MatrixOptions.P))
        self.buttonLMatrix.clicked.connect(lambda: self.setMethodIndex(MatrixOptions.L))
        self.buttonUMatrix.clicked.connect(lambda: self.setMethodIndex(MatrixOptions.U))

        self.OriginalWidget = QWidget()
        self.OriginalWidget.setLayout(self.OriginalMatrix.viewMatrix)
        self.PWidget = QWidget()
        self.PWidget.setLayout(self.PMatrix.viewMatrix)
        self.LWidget = QWidget()
        self.LWidget.setLayout(self.LMatrix.viewMatrix)
        self.UWidget = QWidget()
        self.UWidget.setLayout(self.UMatrix.viewMatrix)

        self.matrixLayout = QStackedLayout()
        self.matrixLayout.addWidget(self.OriginalWidget)
        self.matrixLayout.addWidget(self.PWidget)
        self.matrixLayout.addWidget(self.LWidget)
        self.matrixLayout.addWidget(self.UWidget)

        self.resultLayout = QVBoxLayout()
        self.resultLayout.addLayout(self.matrixOptionsLayout)
        self.resultLayout.addLayout(self.matrixLayout)

        self.setLayout(self.resultLayout)

    def setMethodIndex(self, caseButton):
        if caseButton == MatrixOptions.Original:
            MethodIndex = 0
        elif caseButton == MatrixOptions.P:
            MethodIndex = 1
        elif caseButton == MatrixOptions.L:
            MethodIndex = 2
        elif caseButton == MatrixOptions.U:
            MethodIndex = 3

        self.matrixLayout.setCurrentIndex(MethodIndex)

    def showPButton(self):
        if(self.dataApp.isPTLU):
            self.buttonPMatrix.setHidden(False)
        else:
            self.buttonPMatrix.setHidden(True)

    def setMatrix(self):
        self.OriginalMatrix.sizeMatrix = self.dataApp.size
        self.OriginalMatrix.matrix = self.dataApp.initMatrix
        self.OriginalMatrix.showMatrix()

        if(self.dataApp.isPTLU):
            self.PMatrix.sizeMatrix = self.dataApp.size
            self.PMatrix.matrix = self.dataApp.PMatrix
            self.PMatrix.showMatrix()

        self.LMatrix.sizeMatrix = self.dataApp.size
        self.LMatrix.matrix = self.dataApp.LMatrix
        self.LMatrix.showMatrix()

        self.UMatrix.sizeMatrix = self.dataApp.size
        self.UMatrix.matrix = self.dataApp.UMatrix
        self.UMatrix.showMatrix()
