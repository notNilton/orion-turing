# functions.py

import argparse
import time
from itertools import permutations
from queue import PriorityQueue

import numpy as np
from scipy.signal import convolve2d as conv2

from utils.classes import State

def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Solve the 8-puzzle or generate solvable states.")
    parser.add_argument("--simple", action="store_true", help="Display only execution time, states explored, path length, and start state.")
    parser.add_argument("--detail", action="store_true", help="Display the full solution path and steps.")
    parser.add_argument("--gendata", action="store_true", help="Generate all solvable puzzle states and store them in a database.")
    return parser.parse_args()

def hamming_heuristic(state: State):
    """
    Computes the Hamming distance between the state's matrix and the goal configuration.
    """
    goal_matrix = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
    misplaced_count = len(state.matrix[np.where(state.matrix != goal_matrix)])
    return (misplaced_count - 1) if misplaced_count > 0 else 0

def is_solvable(state: State) -> bool:
    """
    Determines if the given N-puzzle state is solvable.
    """
    flat_matrix = state.matrix.flatten()
    flat_matrix = flat_matrix[flat_matrix != 9]  # Remove the blank tile

    inversions = 0
    for i in range(len(flat_matrix)):
        for j in range(i + 1, len(flat_matrix)):
            if flat_matrix[i] > flat_matrix[j]:
                inversions += 1

    blank_row = np.where(state.matrix == 9)[0][0]
    grid_size = state.matrix.shape[0]

    if grid_size % 2 == 1:  # Odd grid (e.g., 3x3)
        return inversions % 2 == 0
    else:  # Even grid (e.g., 4x4)
        if (blank_row % 2 == 0 and inversions % 2 == 1) or (blank_row % 2 == 1 and inversions % 2 == 0):
            return True
        else:
            return False

def generate_all_states():
    """
    Generates all possible initial states for the 8-puzzle.
    """
    tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 9 represents the blank tile
    all_permutations = permutations(tiles)
    return [np.array(perm).reshape(3, 3) for perm in all_permutations]

def allowed_moves(state: State):
    """
    Returns the permitted moves based on the current state.
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

def performance_analysis(func):
    """
    Decorator to measure the execution time and count the number of states explored.
    """
    def wrapper(*args, **kwargs):
        # Start timing
        start_time = time.time()
        
        # Initialize performance metrics
        wrapper.states_explored = 0
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        
        # Print performance metrics
        print(f"Performance Analysis for {func.__name__}:")
        print(f"  - Execution Time: {elapsed_time:.4f} seconds")
        print(f"  - States Explored: {wrapper.states_explored}")
        print(f"  - Path Length: {result.path_length if hasattr(result, 'path_length') else 'N/A'}")
        
        return result
    return wrapper

def astar_heuristic(initial_state: State, heuristic, goal: State):
    """
    Performs the A* search algorithm to find a path from the initial state to the goal state.
    """
    open_set = PriorityQueue()
    initial_state.priority = 0
    open_set.put((initial_state.priority, initial_state))

    while not open_set.empty():
        current_state = open_set.get()[1]
        
        # Increment states explored counter
        astar_heuristic.states_explored += 1

        if current_state == goal:
            return current_state

        for tile in allowed_moves(current_state):
            next_state = move(current_state, tile)
            next_state.path_length = current_state.path_length + 1
            next_state.parent = current_state
            next_state.priority = heuristic(next_state) + next_state.path_length
            open_set.put((next_state.priority, next_state))

    return initial_state
