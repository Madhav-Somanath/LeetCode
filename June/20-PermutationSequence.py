"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note:

    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.
"""

# SOLUTION

def getPermutation(n: int, k: int) -> str:
    
    res, nums = "",  [i for i in range(1, n+1)]
    k -= 1
    
    while n:
        n -= 1
        index, k = divmod(k, math.factorial(n))
        res += str(nums.pop(index))
    return res

# attempting all permutations (probably not the most optimum)