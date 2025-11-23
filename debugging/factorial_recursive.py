#!/usr/bin/python3

import sys

def factorial(n):
    """
    Function Description:
        Recursively calculates the factorial of a number. The function calls
        itself with decreasing values until it reaches the base case.

    Parameters:
        n (int): A non-negative integer whose factorial will be computed.

    Returns:
        int: The resulting factorial value for the number provided.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Convert command-line input to an integer and compute its factorial
f = factorial(int(sys.argv[1]))
print(f)
