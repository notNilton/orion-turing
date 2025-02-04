# utils/estado.py

import numpy as np

class Estado:
    def __init__(self, pai=None, matriz=None):
        self.pai = pai
        self.matriz = matriz

        self.d = 0  # tamanho do caminho do início ao estado atual
        self.c = 0  #
        self.p = 0  # prioridade

    def __eq__(self, other):
        return len(self.matriz[np.where(self.matriz != other.matriz)]) == 0

    def __lt__(self, other):
        return self.p < other.p

    def mostrar(self):
        for i in self.matriz:
            print(i)
        print()
