# utils/init.py

from utils.classes import State
import numpy as np

def initialize_states(start_matrix=None, goal_matrix=None):
    """
    Initializes the start and goal states for the 8-puzzle.

    Parameters:
        start_matrix (np.ndarray, optional): Custom initial state matrix.
        goal_matrix (np.ndarray, optional): Custom goal state matrix.

    Returns:
        tuple: (goal_state, start_state)
    """
    default_goal = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])

    default_start = np.array([[1, 2, 3],
                               [4, 9, 5],
                               [7, 8, 6]])

    goal_state = State(matrix=goal_matrix if goal_matrix is not None else default_goal)
    start_state = State(matrix=start_matrix if start_matrix is not None else default_start)

    return goal_state, start_state

