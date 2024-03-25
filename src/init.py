import sys
from PySide6 import QtCore, QtWidgets, QtGui

# Files
from Screens import InitScreen, InsertionMatrix, Calculation, Result

class Controller(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle('Proyecto - Algebra Lineal 2024-1')

        self.stacked = QtWidgets.QStackedWidget(self)

        self.setCentralWidget(self.stacked)

        self.widget1 = InitScreen.InitScreen()
        self.stacked.addWidget(self.widget1)

        self.widget2 = InsertionMatrix.InsertionMatrix()
        self.stacked.addWidget(self.widget2)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mainWindow = Controller()
    mainWindow.show()

    sys.exit(app.exec())
