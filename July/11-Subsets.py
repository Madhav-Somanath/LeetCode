""" Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets. """

# SOLUTION

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result
    
# iterative solution, can also be done by DFS