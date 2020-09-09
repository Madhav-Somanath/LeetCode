""" You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer. """

# SOLUTION

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1 + 8*n) ** 0.5) // 2)
    
# According to sum of arithmetic series formula: 1 + 2 + 3 + ... + k = (1 + k) * k/ 2
# We can make quadratic equation out of it: (1 + k) * k/ 2 = n
# Meaning:
# k^2 + k - 2 * n = 0
# Which corresponds to general quadratic equation form:
# ax^2 + bx + c = 0
# By quadratic formula we can find: k = -b + sqrt(b^2 - 4ac)/2a
# Which in our case is: k = -1 + sqrt(1 + 8n)/2

# Answer is the solution of the equation taking the floor int value.

"""
k = 1
        
while n >= 0:
    n -= k
    k += 1
    
return k - 2

"""