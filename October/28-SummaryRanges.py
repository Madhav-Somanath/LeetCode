""" You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, result, N = 0, [], len(nums)
        
        while i < N:
            beg = end = i
            while end < N - 1 and nums[end] + 1 == nums[end + 1]:
                end += 1
                
            result.append(str(nums[beg]) + ("->" + str(nums[end])) *(beg != end))     
            i = end + 1
        
        return result