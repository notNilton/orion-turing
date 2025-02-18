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
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Solve the 8-puzzle or generate solvable states."
    )
    parser.add_argument(
        "--simple",
        action="store_true",
        help="Display only execution time, states explored, path length, and start state.",
    )
    parser.add_argument(
        "--detail",
        action="store_true",
        help="Display the full solution path and steps.",
    )
    parser.add_argument(
        "--gendata",
        action="store_true",
        help="Generate all possible 8-puzzle states and store only solvable ones in the database.",
    )
    parser.add_argument(
        "--db_path",
        type=str,
        default="data/puzzle_states.db",
        help="Specify a custom path for the SQLite database.",
    )
    parser.add_argument(
        "--store_all",
        action="store_true",
        help="Store all generated states instead of only the solvable ones.",
    )
    return parser.parse_args()

def hamming_heuristic(state: State) -> int:
    """
    Computes the Hamming distance between the state's matrix and the goal configuration.

    Parameters:
        state (State): The current puzzle state.

    Returns:
        int: Number of misplaced tiles (excluding the blank space).
    """
    goal_matrix = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])
    misplaced_count = np.sum(state.matrix != goal_matrix) - 1
    return max(misplaced_count, 0)

def is_solvable(state: State) -> bool:
    """
    Determines if the given N-puzzle state is solvable.

    Parameters:
        state (State): The puzzle state.

    Returns:
        bool: True if the puzzle is solvable, False otherwise.
    """
    flat_matrix = state.matrix.flatten()
    flat_matrix = flat_matrix[flat_matrix != 9]  # Remove the blank tile

    inversions = sum(
        1 for i in range(len(flat_matrix)) for j in range(i + 1, len(flat_matrix))
        if flat_matrix[i] > flat_matrix[j]
    )

    blank_row = np.where(state.matrix == 9)[0][0]
    grid_size = state.matrix.shape[0]

    return (inversions % 2 == 0) if (grid_size % 2 == 1) else (
        (blank_row % 2 == 0 and inversions % 2 == 1) or (blank_row % 2 == 1 and inversions % 2 == 0)
    )

def generate_all_states() -> list:
    """
    Generates all possible initial states for the 8-puzzle.

    Returns:
        list: A list of all possible 8-puzzle states as 3x3 numpy arrays.
    """
    tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 9 represents the blank tile
    return [np.array(perm).reshape(3, 3) for perm in permutations(tiles)]

def allowed_moves(state: State) -> list:
    """
    Returns the permitted moves based on the current state.

    Parameters:
        state (State): The puzzle state.

    Returns:
        list: List of valid tiles that can be moved.
    """
    adjacency = np.array([[0, 1, 0],
                          [1, 0, 1],
                          [0, 1, 0]])
    blank = state.matrix == 9
    mask = conv2(blank, adjacency, mode="same")
    return state.matrix[np.where(mask)]

def move(state: State, tile: int) -> State:
    """
    Moves the specified tile in the given state.

    Parameters:
        state (State): The current puzzle state.
        tile (int): The tile to move.

    Returns:
        State: The new puzzle state after the move.
    """
    new_matrix = state.matrix.copy()
    new_matrix[np.where(state.matrix == 9)] = tile
    new_matrix[np.where(state.matrix == tile)] = 9
    return State(matrix=new_matrix)

def astar_heuristic(initial_state: State, heuristic, goal: State) -> State:
    """
    Performs the A* search algorithm to find a path from the initial state to the goal state.

    Parameters:
        initial_state (State): The initial state of the puzzle.
        heuristic (function): The heuristic function to use.
        goal (State): The goal state of the puzzle.

    Returns:
        State: The final state if a path is found; otherwise, the initial state.
    """
    open_set = PriorityQueue()
    initial_state.priority = 0
    open_set.put((initial_state.priority, initial_state))

    while not open_set.empty():
        current_state = open_set.get()[1]
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

def display_simple_output(execution_time: float, states_explored: int, solution_path: list, start_state: State):
    """
    Displays a concise output including execution time, explored states, and path length.

    Parameters:
        execution_time (float): Time taken to solve the puzzle.
        states_explored (int): Number of states explored by A*.
        solution_path (list): List of states in the solution path.
        start_state (State): The initial state.
    """
    print("- Execution Time: {:.4f} seconds".format(execution_time))
    print("- States Explored:", states_explored)
    print("- Path Length:", len(solution_path) - 1)
    print("- Start State:", start_state.matrix.flatten().tolist())

def display_detailed_output(solution_path: list):
    """
    Displays the full solution path.

    Parameters:
        solution_path (list): List of states in the solution path.
    """
    print("\nSolution found!")
    print("Number of steps:", len(solution_path) - 1)
    print("Solution path:\n")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        state.display()
        print()
