# main.py

import numpy as np
from utils.classes import State
from functions.functions import hamming_heuristic, astar_heuristic

def main():
    goal_state = State(matrix=np.array([[1, 2, 3],
                                        [4, 5, 6],
                                        [7, 8, 9]]))
    start_state = State(matrix=np.array([[1, 2, 3],
                                        [4, 9, 5],
                                        [7, 8, 6]]))
    result_state = astar_heuristic(start_state, hamming_heuristic, goal_state)
    result_state.display()
    print(result_state.path_length)

if __name__ == "__main__":
    main()
