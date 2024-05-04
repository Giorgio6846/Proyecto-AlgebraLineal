from PySide6.QtWidgets import QWidget, QFormLayout, QHBoxLayout, QLabel

class matrixShow(QWidget):
    def __init__(self):
        self.matrix = [];
        self.sizeMatrix = 0;

        self.viewMatrix = QFormLayout()
        self.MatrixInfo = []

        self.initMatrix()

    def initMatrix(self):
        for column in range(0, 10):
            self.MatrixRowInfo = []
            self.MatrixRowLayout = QHBoxLayout()
            for row in range(0,10):
                self.cellMatrix = QLabel()
                self.cellMatrix.setText("1")

                self.MatrixRowLayout.addWidget(self.cellMatrix)
                self.MatrixRowInfo.append(self.cellMatrix)
            self.viewMatrix.addRow(self.MatrixRowLayout)
            self.MatrixInfo.append(self.MatrixRowInfo)
        
        self.hideMatrix()

    def hideMatrix(self):
        for row in self.MatrixInfo:
            for col in row:
                col.setHidden(True)

    def showMatrix(self):
        self.hideMatrix()

        for row in range(0, self.sizeMatrix):
            for col in range(0, self.sizeMatrix):
                self.MatrixInfo[row][col].setText(str(self.matrix[row][col]))
                self.MatrixInfo[row][col].setHidden(False)
