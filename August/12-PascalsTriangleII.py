""" Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0. """

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]*(rowIndex+1)
        
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                res[i-j] += res[i-j-1]
                
        return res