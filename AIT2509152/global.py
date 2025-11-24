import numpy as np

class Matrix:

    def __init__(self, name):
        self.matrix = None
        self.name = name
        self.rows = 0
        self.cols = 0

    def input_matrix(self):
        temp_matrix = []
        self.rows = int(input(f"Enter the number of rows for Matrix {self.name}"))
        self.cols = int(input(f"Enter the number of columns for Matrix {self.name}"))
        for i in range(self.rows):
            rows = input(f"Enter {self.cols} numbers for row {i+1} Matrix {self.name}")

    def transpose(self):
        transposed = np.transpose(self.matrix)
        return transposed