import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStackedLayout, QPushButton
from PySide6.QtGui import QPalette, QColor
from enum import Enum
from Screens import InitScreen, InsertionMatrix, Calculation, Result
import numpy as np

Options = Enum('Options', ['MainScreen', 'ExitProgram', 'InsertData', 'ResultMatrix'])

class Data():
    matrix = []
    size = 0
    matrixReady = []

    LUMethodL = []
    LUMethodU = []
    
    PLUMethodP = []
    PLUMethodL = []
    PLUMethodU = []

    def __init__(self):
        self.matrix = np.zeros(shape=(10,10))

    def setMatrixReady(self, num):
        self.matrixReady = np.zeros(shape=(num, num))

        for row in range(0, num):
            for col in range(0, num):
                self.matrixReady[row][col] = self.matrix[row][col]


class Controller(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.dataApp = Data()

        self.index = 0

        self.LayoutButton = QHBoxLayout()

        self.buttonStart = QPushButton(text = "Menu")
        self.buttonInsertMatrix = QPushButton(text= "Ingreso de datos")
        self.buttonResult = QPushButton(text="Resultado")
        self.buttonExit = QPushButton(text="Salir")

        self.buttonStart.clicked.connect(lambda: self.setIndex(Options.MainScreen))
        self.buttonInsertMatrix.clicked.connect(lambda: self.setIndex(Options.InsertData))
        self.buttonResult.clicked.connect(lambda: self.setIndex(Options.ResultMatrix))
        self.buttonExit.clicked.connect(lambda: self.setIndex(Options.ExitProgram))

        self.LayoutButton.addWidget(self.buttonStart)
        self.LayoutButton.addWidget(self.buttonInsertMatrix)
        self.LayoutButton.addWidget(self.buttonResult)
        self.LayoutButton.addWidget(self.buttonExit)

        self.layout = QStackedLayout()

        self.mainScreen = InitScreen.InitScreen(self.dataApp)
        self.insertionMatrix = InsertionMatrix.InsertionMatrix(self.dataApp)
        self.calculationMatrix = Calculation.Calculation(self.dataApp)
        self.resultMatrix = Result.Result(self.dataApp)

        self.layout.addWidget(self.mainScreen)
        self.layout.addWidget(self.insertionMatrix)
        self.layout.addWidget(self.resultMatrix)

        self.layout.setCurrentIndex(self.index)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.addLayout(self.LayoutButton)
        self.mainLayout.addLayout(self.layout)
        self.setLayout(self.mainLayout)

    def setIndex(self, caseButton):
        if caseButton == Options.ExitProgram:
            sys.exit(app.exec())
        elif caseButton == Options.MainScreen:
            self.index = 0
            self.layout.setCurrentIndex(self.index)
        elif caseButton == Options.InsertData:
            self.index = 1
            self.layout.setCurrentIndex(self.index)
        elif caseButton == Options.ResultMatrix:
            self.index = 2
            self.calculationMatrix.LUCalc()
            
            print(self.dataApp.LUMethodL)
            print(self.dataApp.LUMethodU)
            
            self.layout.setCurrentIndex(self.index)

    def initUI(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle('Proyecto - Algebra Lineal 2024-1')

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = Controller()
    mainWindow.show()
    
    sys.exit(app.exec())
