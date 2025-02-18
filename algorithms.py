# algortihms.py

import numpy as np
from scipy.signal import convolve2d as conv2
from itertools import permutations
from utils.classes import State
import sqlite3
import os
import json

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

def create_database(db_name: str = "puzzle_solutions.db"):
    """
    Creates a SQLite database and a table to store solvable puzzle states.
    If the database or table already exists, it does nothing.
    """
    if not os.path.exists(db_name):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS solvable_states (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                solution TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print(f"Database '{db_name}' created with table 'solvable_states'.")
    else:
        print(f"Database '{db_name}' already exists.")

def add_solution_to_db(state: np.ndarray, db_name: str = "puzzle_solutions.db"):
    """
    Adds a new solvable state to the SQLite database.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Convert the state matrix to a JSON string
    solution_json = json.dumps(state.flatten().tolist())
    
    # Insert the state into the database
    cursor.execute('''
        INSERT INTO solvable_states (solution)
        VALUES (?)
    ''', (solution_json,))
    
    conn.commit()
    conn.close()
    print(f"State added to the database: {solution_json}")