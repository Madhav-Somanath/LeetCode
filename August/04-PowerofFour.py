""" Given an integer (signed 32 bits), write a function to check whether it is a power of 4. """

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        s = bin(num)[3:]
        return num!=0 and ('1' not in s) and len(s)%2 == 0
    
'''
if: x == 4n,
then: x == (22)n, which means: x == 2(2n);
so, for binary, if:
the 1st number is 1,
the rest numbers are all 0,
the length of rest is 2n.
then x must be a power of 4.
'''