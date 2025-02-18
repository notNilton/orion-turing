# main.py

import numpy as np
import time
from utils.classes import State
from functions import hamming_heuristic, is_solvable, parse_arguments, astar_heuristic
from database import generate_and_store_states

def initialize_states():
    goal_state = State(matrix=np.array([[1, 2, 3],
                                        [4, 5, 6],
                                        [7, 8, 9]]))
    start_state = State(matrix=np.array([[1, 2, 3],
                                         [4, 9, 5],
                                         [7, 8, 6]]))
    return goal_state, start_state

def solve_puzzle(start_state, goal_state):
    print("Running A* with Hamming heuristic...\n")
    
    start_time = time.time()
    astar_heuristic.states_explored = 0
    result_state = astar_heuristic(start_state, hamming_heuristic, goal_state)
    execution_time = time.time() - start_time

    return result_state, execution_time

def build_solution_path(result_state):
    solution_path = []
    current = result_state
    while current is not None:
        solution_path.append(current)
        current = current.parent
    solution_path.reverse()
    return solution_path

def display_simple_output(execution_time, states_explored, solution_path, start_state):
    print("- Execution Time: {:.4f} seconds".format(execution_time))
    print("- States Explored:", states_explored)
    print("- Path Length:", len(solution_path) - 1)
    print("- Start State:", start_state.matrix.flatten().tolist())

def display_detailed_output(solution_path):
    print("Solution found!")
    print("Number of steps:", len(solution_path) - 1)
    print("Solution path:\n")
    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        state.display()
        print()

def main():
    args = parse_arguments()

    if args.gendata:
        generate_and_store_states()
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
