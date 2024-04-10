from PySide6.QtWidgets import QWidget, QLabel

class Result(QWidget):

    def __init__(self, data):
        super().__init__()
        self.dataApp = data

