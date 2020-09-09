""" The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance. """

# SOLUTION

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        Out, t = 0, x^y 
        while t:
            t, Out = t & (t-1), Out + 1
        return Out
    
# classic bit manipulation counting method