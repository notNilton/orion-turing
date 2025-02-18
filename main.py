# main.py

import numpy as np
from utils.classes import State
from algorithms import hamming_heuristic, is_solvable
from functions import astar_heuristic

def main():
    # Define o estado objetivo e o estado inicial
    goal_state = State(matrix=np.array([[1, 2, 3],
                                        [4, 5, 6],
                                        [7, 8, 9]]))
    start_state = State(matrix=np.array([[1, 2, 3],
                                        [4, 9, 5],
                                        [7, 8, 6]]))
    
    # Verifica se o puzzle é solucionável
    if not is_solvable(start_state):
        print("Este puzzle não é solucionável.")
        return

    print("Executando A* com heurística de Hamming...\n")
    
    # Executa o A* (o decorator 'performance_analysis' exibirá a duração, estados explorados e o tamanho do caminho)
    result_state = astar_heuristic(start_state, hamming_heuristic, goal_state)

    # Se não encontrar o caminho até o objetivo, informa e encerra
    if result_state != goal_state:
        print("Solução não encontrada.")
        return

    # Reconstrói o caminho da solução a partir do estado final, seguindo os pais
    solution_path = []
    current = result_state
    while current is not None:
        solution_path.append(current)
        current = current.parent
    solution_path.reverse()  # Inverte para que o primeiro elemento seja o estado inicial

    # Exibe a solução e os passos
    print("\nSolução encontrada!")
    print("Número de passos:", len(solution_path) - 1)
    print("Caminho da solução:\n")
    for step, state in enumerate(solution_path):
        print(f"Passo {step}:")
        state.display()  # Supondo que o método display() mostre o estado (por exemplo, imprimindo a matriz)
        print()

if __name__ == "__main__":
    main()
