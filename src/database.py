# database.py 

import json
import os
import sqlite3
from itertools import permutations

import numpy as np

from functions import is_solvable, solve_puzzle, build_solution_path, display_simple_output, astar_heuristic

from utils.classes import State
from utils.init import initialize_states
from setup import DEFAULT_DB_PATH

def create_database(db_path: str = DEFAULT_DB_PATH, table_name: str = "puzzle_states"):
    """
    Creates a SQLite database and a table to store puzzle states.
    If the database or table already exists, it ensures the table exists.

    Parameters:
        db_path (str): Path to the SQLite database file.
        table_name (str): Name of the table to create.
    """
    os.makedirs(os.path.dirname(db_path), exist_ok=True)  # Ensure directory exists

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            array TEXT NOT NULL,
            is_solvable BOOLEAN NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"Database '{db_path}' is ready with table '{table_name}'.")

def generate_and_store_states(
    db_path: str = DEFAULT_DB_PATH,
    table_name: str = "puzzle_states",
    store_only_solvable: bool = True
):
    """
    Generates all possible 8-puzzle initial states, checks if they are solvable,
    and stores them in the database.

    Parameters:
        db_path (str): Path to the SQLite database file.
        table_name (str): Name of the table where states will be stored.
        store_only_solvable (bool): If True, stores only solvable states; otherwise, stores all states.
    """
    create_database(db_path, table_name)  # Ensure table exists before inserting data

    tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 9 represents the empty tile
    all_permutations = permutations(tiles)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    total_count = 0
    solvable_count = 0

    for perm in all_permutations:
        state_matrix = np.array(perm).reshape(3, 3)
        state = State(matrix=state_matrix)
        solvable = is_solvable(state)

        if store_only_solvable and not solvable:
            continue  # Skip unsolvable states

        total_count += 1
        if solvable:
            solvable_count += 1
        
        cursor.execute(f'''
            INSERT INTO {table_name} (array, is_solvable)
            VALUES (?, ?)
        ''', (json.dumps(state_matrix.tolist()), solvable))

    conn.commit()
    conn.close()
    print(f"Stored {solvable_count} solvable states out of {total_count} total states in '{db_path}'.")

def testdata(db_path: str = DEFAULT_DB_PATH, table_name: str = "puzzle_states"):
    """
    Runs the pathfinding algorithm on all stored solvable states from the database efficiently.

    Parameters:
        db_path (str): Path to the SQLite database file.
        table_name (str): Name of the table containing stored puzzle states.
    """
    
    # Connect to database and fetch all solvable states
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT array FROM {table_name} WHERE is_solvable = 1")
    stored_states = cursor.fetchall()
    conn.close()

    total_states = len(stored_states)

    if not stored_states:
        print("No solvable states found in the database.")
        return

    print(f"Running A* on {total_states} stored solvable states...\n")

    goal_state, _ = initialize_states()

    for i in range(total_states):
        state_data = stored_states.pop(0)  # Remove the first element to free memory
        start_matrix = np.array(json.loads(state_data[0]))
        start_state = State(matrix=start_matrix)

        result_state, execution_time = solve_puzzle(start_state, goal_state)

        if result_state != goal_state:
            print(f"Test {i + 1}/{total_states}: Solution not found.")
            continue

        solution_path = build_solution_path(result_state)

        # Show progress instead of printing full details every time
        if (i + 1) % 1000 == 0 or i == total_states - 1:
            print(f"Processed {i + 1}/{total_states} states...")

    print("\nFinished running tests on all stored solvable states.")
