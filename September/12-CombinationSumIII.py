""" Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

    All numbers will be positive integers.
    The solution set must not contain duplicate combinations.
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        l=list(combinations([i for i in range(1, 10)], k))
        for i in l:
            if sum(i)==n:
                res.append(list(i))
        return res
    
'''
self.ans = []
def dfs(start, sol, k, n):
    if k == 0 and n == 0:
        self.ans.append(sol)
    if start > 9 or start > n or k <= 0:
        return
    dfs(start+1, sol+[start], k-1, n-start)
    dfs(start+1, sol, k, n)
dfs(1, [], k, n)
return self.ans
'''