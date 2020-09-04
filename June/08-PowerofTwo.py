"""
Given an integer, write a function to determine if it is a power of two.
"""

# SOLUTION

def isPowerOfTwo(n: int) -> bool:
    return n > 0 and n&(n-1) == 0

# time complexity O(1), we can also divide and check in O(log(n)) time (iterative and recursice)