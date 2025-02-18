# main.py

import numpy as np
import argparse
import time
from utils.classes import State
from algorithms import hamming_heuristic, is_solvable
from functions import astar_heuristic

def main():
    parser = argparse.ArgumentParser(description="Solve the 8-puzzle using A* search with Hamming heuristic.")
    parser.add_argument("--simple", action="store_true", help="Display only execution time, states explored, path length, and start state.")
    parser.add_argument("--detail", action="store_true", help="Display the full solution path and steps.")
    args = parser.parse_args()

    goal_state = State(matrix=np.array([[1, 2, 3],
                                        [4, 5, 6],
                                        [7, 8, 9]]))
    start_state = State(matrix=np.array([[1, 2, 3],
                                         [4, 9, 5],
                                         [7, 8, 6]]))
    
    if not is_solvable(start_state):
        print("This puzzle is not solvable.")
        return

    print("Running A* with Hamming heuristic...\n")
    
    start_time = time.time()
    astar_heuristic.states_explored = 0
    result_state = astar_heuristic(start_state, hamming_heuristic, goal_state)
    execution_time = time.time() - start_time

    if result_state != goal_state:
        print("Solution not found.")
        return

    solution_path = []
    current = result_state
    while current is not None:
        solution_path.append(current)
        current = current.parent
    solution_path.reverse()

    if args.simple:
        print("- Execution Time: {:.4f} seconds".format(execution_time))
        print("- States Explored:", astar_heuristic.states_explored)
        print("- Path Length:", len(solution_path) - 1)
        print("- Start State:", start_state.matrix.flatten().tolist())

    elif args.detail:
        print("\nSolution found!")
        print("Number of steps:", len(solution_path) - 1)
        print("Solution path:\n")
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            state.display()
            print()
    else:
        print("\nUse --simple for a concise output or --detail for a detailed output.")

if __name__ == "__main__":
    main()
