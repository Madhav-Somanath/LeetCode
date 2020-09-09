""" Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition. """

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        res = []
        
        for val in A:
            if val % 2 == 1:
                res.append(val)
            else:
                res.insert(0,val)
                
        return res