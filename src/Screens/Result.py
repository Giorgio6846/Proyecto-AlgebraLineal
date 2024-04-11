from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
    QHBoxLayout,
    QPushButton,
    QInputDialog,
    QStackedLayout,
    QFormLayout)

from PySide6.QtGui import QFont
from PySide6.QtCore import *
import random
from enum import Enum

Methods = Enum("Methods", ["LU", "PLU"])
LUMethod = Enum("LUMethod", ["L", "U"])
PLUMethod = Enum("PLUMethod", ["P", "L", "U"])

class Result(QWidget):

    def __init__(self, data):
        super().__init__()
        self.dataApp = data

        self.LUUMatrixForm = QFormLayout()
        self.LULMatrixForm = QFormLayout()

        self.LayoutMethodsButton = QHBoxLayout()
        self.buttonPLUMethod = QPushButton(text = "PLU")
        self.buttonLUMethod = QPushButton(text="LU")

        self.LayoutMethodsButton.addWidget(self.buttonLUMethod)
        self.LayoutMethodsButton.addWidget(self.buttonPLUMethod)

        self.buttonPLUMethod.clicked.connect(lambda: self.setMethodIndex(Methods.PLU))
        self.buttonLUMethod.clicked.connect(lambda: self.setMethodIndex(Methods.LU))

        # LU Method
        self.LUWidget = QWidget()
        self.LUMethodLayout = QStackedLayout()
        self.LUButtons = QHBoxLayout()
        self.LbuttonLUMethod = QPushButton(text="L")
        self.UbuttonLUMethod = QPushButton(text="U")

        self.LbuttonLUMethod.clicked.connect(lambda: self.setLUMethodIndex(LUMethod.L))
        self.UbuttonLUMethod.clicked.connect(lambda: self.setLUMethodIndex(LUMethod.U))

        self.LUButtons.addWidget(self.LbuttonLUMethod)
        self.LUButtons.addWidget(self.UbuttonLUMethod)

        self.LULayout = QVBoxLayout()
        self.LULayout.addLayout(self.LUButtons)
        self.LULayout.addLayout(self.LUMethodLayout)

        self.LULWidget = QWidget()
        self.LULWidget.setLayout(self.LULMatrixForm)

        self.LUUWidget = QWidget()
        self.LUUWidget.setLayout(self.LUUMatrixForm)

        self.LUMethodLayout.addWidget(self.LULWidget)
        self.LUMethodLayout.addWidget(self.LUUWidget)

        self.LUWidget.setLayout(self.LULayout)

        # PLU Method
        self.PLUWidget = QWidget()
        self.PLUMethodLayout = QStackedLayout()
        self.PLUButtons = QHBoxLayout()
        self.PbuttonPLUMethod = QPushButton(text="P")
        self.LbuttonPLUMethod = QPushButton(text="L")
        self.UbuttonPLUMethod = QPushButton(text="U")

        self.PbuttonPLUMethod.clicked.connect(lambda: self.setLUMethodIndex(PLUMethod.P))
        self.LbuttonPLUMethod.clicked.connect(lambda: self.setLUMethodIndex(PLUMethod.L))
        self.UbuttonPLUMethod.clicked.connect(lambda: self.setLUMethodIndex(PLUMethod.U))

        self.PLUButtons.addWidget(self.PbuttonPLUMethod)
        self.PLUButtons.addWidget(self.LbuttonPLUMethod)
        self.PLUButtons.addWidget(self.UbuttonPLUMethod)

        self.PLULayout = QVBoxLayout()
        self.PLULayout.addLayout(self.PLUButtons)
        self.PLULayout.addLayout(self.PLUMethodLayout)

        self.PLUWidget.setLayout(self.PLULayout)

        self.methodsLayout = QStackedLayout()
        self.methodsLayout.addWidget(self.LUWidget)
        self.methodsLayout.addWidget(self.PLUWidget)

        self.resultLayout = QVBoxLayout()
        self.resultLayout.addLayout(self.LayoutMethodsButton)
        self.resultLayout.addLayout(self.methodsLayout)

        self.setLayout(self.resultLayout)

    def setMethodIndex(self, caseButton):
        if caseButton == Methods.LU:
            MethodIndex = 0
            self.methodsLayout.setCurrentIndex(MethodIndex)

        elif caseButton == Methods.PLU:
            MethodIndex = 1
            self.methodsLayout.setCurrentIndex(MethodIndex)

    def setLUMethodIndex(self, caseButton):
        if caseButton == LUMethod.L:
            MethodIndex = 0
            self.LUMethodLayout.setCurrentIndex(MethodIndex)

        elif caseButton == LUMethod.U:
            MethodIndex = 1
            self.LUMethodLayout.setCurrentIndex(MethodIndex)

    def setPLUMethodIndex(self, caseButton):
        if caseButton == PLUMethod.P:
            MethodIndex = 0
            self.PLUMethodLayout.setCurrentIndex(MethodIndex)

        elif caseButton == PLUMethod.L:
            MethodIndex = 1
            self.PLUMethodLayout.setCurrentIndex(MethodIndex)

        elif caseButton == PLUMethod.U:
            MethodIndex = 2
            self.PLUMethodLayout.setCurrentIndex(MethodIndex)

    def LUMethod(self):
        print()
        # self.LULayout = QStackedLayout()

    def PLUMethod(self):
        print()
        # self.PLUlayout = QStackedLayout()

    def LULinitMatrix(self):
        for column in range(0, self.dataApp.LUMethodU.shape[0]):
            MatrixRowLayout = QHBoxLayout()
            for row in range(0, self.dataApp.LUMethodU.shape[0]):
                cellMatrix = QLabel()
                cellMatrix.setText(str(self.dataApp.LUMethodL[row][column]))
                MatrixRowLayout.addWidget(cellMatrix)
            self.LULMatrixForm.addRow(MatrixRowLayout)

    def LUUinitMatrix(self):
        for column in range(0, self.dataApp.LUMethodL.shape[0]):
            MatrixRowLayout = QHBoxLayout()
            for row in range(0, self.dataApp.LUMethodL.shape[0]):
                cellMatrix = QLabel()
                cellMatrix.setText(str(self.dataApp.LUMethodU[row][column]))
                MatrixRowLayout.addWidget(cellMatrix)
            self.LUUMatrixForm.addRow(MatrixRowLayout)
