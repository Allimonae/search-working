"""   
    Created by Allison Lee on October 7th, 2024
    CSCI 350 Fall 2024 Assignment 4
"""
import sys
from search import NQueensProblem, hill_climbing

def main():
    # Parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: python3 main.py <N> <algorithm>")
        return

    N = int(sys.argv[1])
    algorithm = sys.argv[2]

    # Initialize the NQueensProblem with size N
    problem = NQueensProblem(N)

    print(f"size: {N}")

    if algorithm == 'hill_climbing':
        # Solve using hill climbing
        solution = hill_climbing(problem)

        # Print the board (solution state)
        print(f"board: {','.join(map(str, solution))}")

        # Print the possible actions from the solution state
        actions = problem.actions(solution)
        print(f"actions: {actions}")

        # Print the number of conflicts
        num_conflicts = problem.h(solution)
        print(f"num_conflicts: {num_conflicts}")

        # Check if the solution is the goal
        is_goal = problem.goal_test(solution)
        print(f"is_goal: {is_goal}")

        if is_goal:
            print("Test Passed!")
        else:
            print("Test Failed: False != True : Your program does not print all the correct output.")
    else:
        print(f"Unknown algorithm: {algorithm}")

if __name__ == '__main__':
    main()