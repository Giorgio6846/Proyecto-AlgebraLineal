from PySide6.QtWidgets import QWidget

class Calculation(QWidget):

    def __init__(self, data):
        super().__init__()
        self.dataApp = data