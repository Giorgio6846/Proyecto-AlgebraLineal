from PySide6.QtWidgets import (
    QWidget,
)

from PySide6.QtGui import QFont
from PySide6.QtCore import *
import random
import numpy as np
from scipy.linalg import lu

class Calculation(QWidget):

    def __init__(self, data):
        super().__init__()
        self.dataApp = data

    def CalcLU(self):
        U = np.zeros(shape=self.dataApp.initMatrix.shape)
        L = np.eye(self.dataApp.initMatrix.shape[0])

        matrixTMP = self.dataApp.initMatrix
        matrixTMP = matrixTMP.astype(float)

        for j in range(0, self.dataApp.initMatrix.shape[0] - 1):
            for i in range(j + 1, self.dataApp.initMatrix.shape[0]):
                if matrixTMP[i, j] != 0.0:
                    mult = matrixTMP[i, j] / matrixTMP[j, j]
                    matrixTMP[i, :] = matrixTMP[i, :] - mult * matrixTMP[j, :]
                    L[i, j] = mult

        # U es A después de escalonar
        U = matrixTMP

        np.set_printoptions(suppress=True)

        self.dataApp.LMatrix = L
        self.dataApp.UMatrix = U

        self.dataApp.matrixVerification = np.matmul(
            L[0 : self.dataApp.size, 0 : self.dataApp.size],
            U[0 : self.dataApp.size, 0 : self.dataApp.size],
        )

        self.isPTLU = False

    def validationPTLU(self):
        try:
            _ = np.linalg.cholesky(self.dataApp.initMatrix)
            return True
        except np.linalg.LinAlgError:
            return False

    def CalcPTLU(self):
        # Get the number of rows
        n = self.dataApp.initMatrix.shape[0]

        # Allocate space for P, L, and U
        U = self.dataApp.initMatrix.copy()
        L = np.eye(n, dtype=np.double)
        P = np.eye(n, dtype=np.double)

        # Loop over rows
        for i in range(n):

            # Permute rows if needed
            for k in range(i, n): 
                if ~np.isclose(U[i, i], 0.0):
                    break
                U[[k, k+1]] = U[[k+1, k]]
                P[[k, k+1]] = P[[k+1, k]]

            # Eliminate entries below i with row
            # operations on U and #reverse the row
            # operations to manipulate L
            factor = U[i+1:, i] / U[i, i]
            L[i+1:, i] = factor
            U[i+1:] -= factor[:, np.newaxis] * U[i]

        self.dataApp.PMatrix = P
        self.dataApp.LMatrix = L
        self.dataApp.UMatrix = U

        self.dataApp.matrixVerification = np.matmul(
            P[0 : self.dataApp.size, 0 : self.dataApp.size],
            L[0 : self.dataApp.size, 0 : self.dataApp.size],
        )

        self.dataApp.matrixVerification = np.matmul(
            self.dataApp.matrixVerification,
            U[0 : self.dataApp.size, 0 : self.dataApp.size],
        )

        self.dataApp.isPTLU = True

    def CalcLUorPTLU(self):
        if(self.dataApp.size != 0):
            if(not(self.validationPTLU())):
                self.CalcLU()
            else:
                self.CalcPTLU()
        else:
            print("No input") 
