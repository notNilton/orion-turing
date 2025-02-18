import numpy as np
import time
from utils.classes import State
from functions import (
    hamming_heuristic,
    is_solvable,
    parse_arguments,
    astar_heuristic
)
from database import generate_and_store_states

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

def solve_puzzle(start_state: State, goal_state: State, heuristic=hamming_heuristic):
    """
    Solves the 8-puzzle using A* with a given heuristic.

    Parameters:
        start_state (State): The initial state.
        goal_state (State): The goal state.
        heuristic (function, optional): The heuristic function to use (default: Hamming heuristic).

    Returns:
        tuple: (result_state, execution_time)
    """
    print(f"Running A* with {heuristic.__name__}...\n")
    
    start_time = time.time()
    astar_heuristic.states_explored = 0
    result_state = astar_heuristic(start_state, heuristic, goal_state)
    execution_time = time.time() - start_time

    return result_state, execution_time

def build_solution_path(result_state: State):
    """
    Builds the solution path from the final state.

    Parameters:
        result_state (State): The resulting state from the A* algorithm.

    Returns:
        list: List of states representing the solution path.
    """
    solution_path = []
    current = result_state
    while current is not None:
        solution_path.append(current)
        current = current.parent
    solution_path.reverse()
    return solution_path

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

def main():
    """
    Main function to run the 8-puzzle solver or generate state data.
    """
    args = parse_arguments()

    if args.gendata:
        generate_and_store_states(db_path=args.db_path, store_only_solvable=not args.store_all)
        return

    goal_state, start_state = initialize_states()

    if not is_solvable(start_state):
        print("This puzzle is not solvable.")
        return

    result_state, execution_time = solve_puzzle(start_state, goal_state)

    if result_state != goal_state:
        print("Solution not found.")
        return

    solution_path = build_solution_path(result_state)

    if args.simple:
        display_simple_output(execution_time, astar_heuristic.states_explored, solution_path, start_state)
    elif args.detail:
        display_detailed_output(solution_path)
    else:
        print("\nUse --simple for a concise output, --detail for a detailed output, or --gendata to generate and store all solvable states.")

if __name__ == "__main__":
    main()
