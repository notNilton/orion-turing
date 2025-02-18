# functions.py

import numpy as np
from queue import PriorityQueue
import time
from multiprocessing import Pool, cpu_count
from algorithms import hamming_heuristic, is_solvable, generate_all_states, allowed_moves, move, create_database, add_solution_to_db
from utils.classes import State

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

# @performance_analysis
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

def process_state(matrix):
    """
    Processa um estado individualmente e o adiciona ao banco de dados se for solucionável.
    """
    state = State(matrix=matrix)
    goal_state = State(matrix=np.array([[1, 2, 3],
                                       [4, 5, 6],
                                       [7, 8, 9]]))
    if is_solvable(state):
        result_state = astar_heuristic(state, hamming_heuristic, goal_state)
        if result_state == goal_state:
            add_solution_to_db(matrix)

def solve_and_store_solvable_states(db_name: str = "puzzle_solutions.db"):
    """
    Solves all solvable 8-puzzle states and stores them in a SQLite database using multiprocessing.
    """
    # Create the database (if it doesn't exist)
    create_database(db_name)

    # Generate all possible states
    all_states = generate_all_states()

    # Use multiprocessing to process states in parallel
    with Pool(processes=cpu_count()) as pool:
        pool.map(process_state, all_states)

    print(f"All solvable states have been stored in the database '{db_name}'.")
    