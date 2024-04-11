from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
    QHBoxLayout,
    QPushButton,
    QInputDialog,
    QFormLayout,
)

from PySide6.QtGui import QFont
from PySide6.QtCore import *
import random
import numpy as np


class Calculation(QWidget):

    def __init__(self, data):
        super().__init__()
        self.dataApp = data

    def LUCalc(self):
        U = np.zeros(shape=self.dataApp.matrix.shape)
        L = np.eye(self.dataApp.matrix.shape[0])

        matrixTMP = self.dataApp.matrix
        matrixTMP = matrixTMP.astype(float)

        for j in range(0, self.dataApp.matrix.shape[0] - 1):
            for i in range(j + 1, self.dataApp.matrix.shape[0]):
                if matrixTMP[i, j] != 0.0:
                    mult = matrixTMP[i, j] / matrixTMP[j, j]
                    matrixTMP[i, :] = matrixTMP[i, :] - mult * matrixTMP[j, :]
                    L[i, j] = mult

        # U es A después de escalonar
        U = matrixTMP

        np.set_printoptions(suppress=True)
        
        self.dataApp.LUMethodL = L
        self.dataApp.LUMethodU = U
