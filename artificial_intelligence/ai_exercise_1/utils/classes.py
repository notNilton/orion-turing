# utils/state.py

import numpy as np

class State:
    def __init__(self, parent=None, matrix=None):
        self.parent = parent
        self.matrix = matrix

        self.path_length = 0  # Length of the path from the initial state
        self.cost = 0         # Additional cost (if applicable)
        self.priority = 0     # Priority value

    def __eq__(self, other):
        return len(self.matrix[np.where(self.matrix != other.matrix)]) == 0

    def __lt__(self, other):
        return self.priority < other.priority

    def display(self):
        for row in self.matrix:
            print(row)
        print()
