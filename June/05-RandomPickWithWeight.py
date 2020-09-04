"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.
    
 """
 
 # SOLUTION
import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        
        for i in range(1,self.n):
            w[i] += w[i-1]
        
        self.s = self.w[-1]

    def pickIndex(self) -> int:
        seed = random.randint(1,self.s)
        l,r = 0, self.n-1
        while l<r:
            mid = (l+r)//2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid+1
        return l

    # One liner using built in tools
    
    '''
    def __init__(self, w):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))
        
    '''