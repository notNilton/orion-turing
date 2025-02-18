# main.py

import os

from functions import (
    is_solvable,
    parse_arguments,
    astar_heuristic,
    display_detailed_output,
    display_simple_output,
    solve_puzzle,
    build_solution_path
)

from database import generate_and_store_states, testdata

from utils.init import initialize_states

def main():
    """
    Main function to run the 8-puzzle solver, generate state data, or test stored states.
    """
    args = parse_arguments()

    if args.gendata:
        generate_and_store_states(db_path=args.db_path, store_only_solvable=not args.store_all)
        return

    if args.testdata:
        testdata()
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
        print("\nUse --simple for a concise output, --detail for a detailed output, --gendata to generate and store all solvable states, or --testdata to test all stored solvable states.")

if __name__ == "__main__":
    main()
