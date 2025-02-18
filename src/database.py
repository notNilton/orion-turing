# database.py 

import json
import os
import sqlite3
from itertools import permutations

import numpy as np

from functions import is_solvable
from utils.classes import State

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "puzzle_states.db")

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
