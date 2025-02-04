# main.py

import numpy as np
from utils.estado import Estado
from functions.functions import acoes_permitidas, movimentar

def main():
    # Exemplo de comparação entre estados
    estado = Estado(matriz=np.array([[4, 1, 3], [9, 2, 5], [7, 8, 6]]))
    estado.p = 1
    estado2 = Estado(matriz=np.array([[4, 1, 3], [9, 2, 5], [7, 8, 6]]))
    estado2.p = 2
    print("Comparação de estados (estado < estado2):", estado < estado2)
    estado.mostrar()

    # Exemplo de uso das funções de ação
    print("Possíveis Ações")
    s = Estado(matriz=np.array([[1, 2, 3], [4, 9, 5], [7, 8, 6]]))
    s.mostrar()
    for acao in acoes_permitidas(s):
        v = movimentar(s, acao)
        v.mostrar()

if __name__ == "__main__":
    main()
