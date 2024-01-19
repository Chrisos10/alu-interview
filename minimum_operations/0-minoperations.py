#!/usr/bin/python3

"""
Defining a function that returns the minimum number of
operations required to have n H characters
"""

def minOperations(n):
    '''
    Function that returns the number of operations
    When n is impossible return 0
    '''
    if n <= 1:
        return 0
    for i in range(2, n+1):
        if (n % i) == 0:
            updated_n = n // i
            operations = i
            break
    return operations + minOperations(updated_n)
