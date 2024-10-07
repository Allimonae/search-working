"""   
    Created by Allison Lee on October 7th, 2024
    CSCI 350 Fall 2024 Assignment 4
"""
import sys
from search import NQueensProblem, hill_climbing

def parse_arguments():
    if len(sys.argv) < 3:
        print("Usage: python main.py <N> <algorithm>")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for N.")
        sys.exit(1)

    algorithm = sys.argv[2]
    return N, algorithm

def main():
    N, algorithm = parse_arguments()

    # Create an instance of NQueensProblem
    problem = NQueensProblem(N)

    # Choose the search algorithm based on user input
    if algorithm == "hill_climbing":
        solution = hill_climbing(problem)
    else:
        print(f"Unknown algorithm: {algorithm}")
        sys.exit(1)

    if solution:
        print("Solution found:", solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()