from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
    QHBoxLayout,
    QPushButton,
    QInputDialog,
    QFormLayout
)
from PySide6.QtGui import QFont
from PySide6.QtCore import *

class InsertionMatrix(QWidget):

    def __init__(self):
        super().__init__()
        
        self.MatrixForm = QFormLayout()
        self.MatrixRowsInput = []
        self.MatrixData = []

        self.initMatrix()

        self.TitleScreen = QLabel("Ingreso de matriz")
        self.TitleScreen.setFont(QFont("Arial", 24))
        self.TitleScreen.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.TitleScreen.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.TitleScreen.setFixedHeight(30)

        self.SizeData = QInputDialog()
        self.SizeData.setLabelText("Ingrese el tamaño de la matriz entre 4 a 10")
        self.SizeData.setInputMode(QInputDialog.IntInput)
        self.SizeData.setIntRange(4,10)

        self.LayoutSize = QHBoxLayout()
        self.LayoutSize.addWidget(self.SizeData)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.TitleScreen)
        self.layout.addLayout(self.LayoutSize)
        self.layout.addLayout(self.MatrixForm)
        self.setLayout(self.layout)

    def initMatrix(self):
        for column in range(0, 10):
            self.MatrixRowInput = []
            self.MatrixRowLayout = QHBoxLayout()
            for row in range(0, 10):
                self.cellMatrix = QInputDialog()
                self.cellMatrix.setOption(QInputDialog.NoButtons)
                self.cellMatrix.setInputMode(QInputDialog.IntInput)
                self.cellMatrix.setLabelText("")
                self.MatrixRowLayout.addWidget(self.cellMatrix)
                self.MatrixRowInput.append(self.cellMatrix)
            self.MatrixForm.addRow(self.MatrixRowLayout)
            self.MatrixRowsInput.append(self.MatrixRowInput)                            
    def showMatrix(self, size):
        print("")
