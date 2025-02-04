# functions/functions.py

from queue import PriorityQueue
import numpy as np
from scipy.signal import convolve2d as conv2
from utils.classes import State

def allowed_moves(state: State):
    """
    Returns the permitted moves based on the current state.
    
    This function identifies the tiles adjacent to the blank (represented by 9)
    in the state's matrix.
    """
    adjacency = np.array([[0, 1, 0],
                          [1, 0, 1],
                          [0, 1, 0]])
    blank = state.matrix == 9
    mask = conv2(blank, adjacency, mode='same')
    return state.matrix[np.where(mask)]

def move(state: State, tile: int) -> State:
    """
    Performs the move of the specified tile in the given state.
    """
    new_matrix = state.matrix.copy()
    new_matrix[np.where(state.matrix == 9)] = tile
    new_matrix[np.where(state.matrix == tile)] = 9
    return State(matrix=new_matrix)

def hamming_heuristic(state: State):
    """
    Computes the Hamming distance between the state's matrix and the goal configuration,
    ignoring the blank tile (represented by 9).
    """
    goal_matrix = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
    misplaced_count = len(state.matrix[np.where(state.matrix != goal_matrix)])
    # Exclude the blank tile from the count
    return (misplaced_count - 1) if misplaced_count > 0 else 0
  
def astar_heuristic(initial_state: State, heuristic, goal: State):
    """
    Performs the A* search algorithm to find a path from the initial state to the goal state.
    
    :param initial_state: The starting state.
    :param heuristic: A function that computes the heuristic value for a given state.
    :param goal: The target state.
    :return: The goal state if reached; otherwise, returns the initial state.
    """
    open_set = PriorityQueue()
    initial_state.priority = 0
    open_set.put((initial_state.priority, initial_state))

    while not open_set.empty():
        current_state = open_set.get()[1]

        if current_state == goal:
            return current_state

        for tile in allowed_moves(current_state):
            next_state = move(current_state, tile)
            next_state.path_length = current_state.path_length + 1
            next_state.parent = current_state
            next_state.priority = heuristic(next_state) + next_state.path_length
            open_set.put((next_state.priority, next_state))

    return initial_state
