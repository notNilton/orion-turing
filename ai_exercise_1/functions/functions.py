# functions/functions.py

import numpy as np
from scipy.signal import convolve2d as conv2
from utils.estado import Estado

def acoes_permitidas(estado: Estado):
    """
    Retorna as ações permitidas com base no estado.
    """
    adj = np.array([[0, 1, 0],
                    [1, 0, 1],
                    [0, 1, 0]])
    blank = estado.matriz == 9
    mask = conv2(blank, adj, 'same')
    return estado.matriz[np.where(mask)]

def movimentar(s: Estado, c: int) -> Estado:
    """
    Realiza a movimentação do elemento indicado no estado.
    """
    matriz = s.matriz.copy()
    matriz[np.where(s.matriz == 9)] = c
    matriz[np.where(s.matriz == c)] = 9
    return Estado(matriz=matriz)
