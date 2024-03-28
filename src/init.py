import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStackedLayout
from PySide6.QtGui import QPalette, QColor

# Files
from Screens import InitScreen, InsertionMatrix, Calculation, Result

class Controller(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.index = 0

        layout = QStackedLayout()

        self.mainScreen = InitScreen.InitScreen(self.index)
        self.insertionMatrix = InsertionMatrix.InsertionMatrix(self.index)
        self.calculationMatrix = Calculation.Calculation(self.index)
        self.resultMatrix = Result.Result(self.index)

        layout.addWidget(self.mainScreen)
        layout.addWidget(self.insertionMatrix)
        layout.addWidget(self.calculationMatrix)
        layout.addWidget(self.resultMatrix)

        layout.setCurrentIndex(self.index)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.addLayout(layout)
        self.setLayout(self.mainLayout)

    def initUI(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle('Proyecto - Algebra Lineal 2024-1')


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = Controller()
    mainWindow.show()
    
    sys.exit(app.exec())
