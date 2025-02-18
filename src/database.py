# database.py 

import json
import os
import sqlite3
from itertools import permutations

import numpy as np

from functions import is_solvable
from utils.classes import State

DB_NAME = "../data/puzzle_states.db"

def create_database(db_name: str = DB_NAME):
    """
    Creates a SQLite database and a table to store puzzle states.
    If the database or table already exists, it ensures the table exists.
    """
    os.makedirs(os.path.dirname(db_name), exist_ok=True)  # Garante que o diretório existe

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS puzzle_states (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            array TEXT NOT NULL,
            is_solvable BOOLEAN NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' is ready with table 'puzzle_states'.")

def generate_and_store_states(db_name: str = DB_NAME):
    """
    Generates all possible 8-puzzle initial states, checks if they are solvable,
    and stores them in the database.
    """
    create_database(db_name)  # Garante que a tabela existe antes da inserção

    tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 9 representa o espaço vazio
    all_permutations = permutations(tiles)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    solvable_count = 0

    for perm in all_permutations:
        state_matrix = np.array(perm).reshape(3, 3)
        state = State(matrix=state_matrix)
        solvable = is_solvable(state)

        if solvable:
            solvable_count += 1
            cursor.execute('''
                INSERT INTO puzzle_states (array, is_solvable)
                VALUES (?, ?)
            ''', (json.dumps(state_matrix.tolist()), True))

    conn.commit()
    conn.close()
    print(f"Stored {solvable_count} solvable states in the database '{db_name}'.")
