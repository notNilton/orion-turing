# main.py

import numpy as np
from utils.classes import State
from algorithms import hamming_heuristic, is_solvable
from functions import astar_heuristic

def main():
    goal_state = State(matrix=np.array([[1, 2, 3],
                                        [4, 5, 6],
                                        [7, 8, 9]]))
    start_state = State(matrix=np.array([[1, 2, 3],
                                        [4, 9, 5],
                                        [7, 8, 6]]))
    
    if not is_solvable(start_state):
        print("Este puzzle não é solucionável.")
        return

    print("Executando A* com heurística de Hamming...\n")
    
    result_state = astar_heuristic(start_state, hamming_heuristic, goal_state)

    if result_state != goal_state:
        print("Solução não encontrada.")
        return

    solution_path = []
    current = result_state
    while current is not None:
        solution_path.append(current)
        current = current.parent
    solution_path.reverse()

    print("\nSolução encontrada!")
    print("Número de passos:", len(solution_path) - 1)
    print("Caminho da solução:\n")
    for step, state in enumerate(solution_path):
        print(f"Passo {step}:")
        state.display()
        print()

if __name__ == "__main__":
    main()
