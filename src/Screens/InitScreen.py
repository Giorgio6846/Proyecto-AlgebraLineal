from PySide6 import QtCore, QtWidgets, QtGui

class InitScreen(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()  
        
        self.screen()
        
    def screen(self):
        self.TitleScreen = QtWidgets.QLabel()
        self.TitleScreen.text = "Proyecto Algebra Lineal"