""" Given an unsorted integer array, find the smallest missing positive integer. """

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 1
        
        ans = float('inf')
        for i in range(1, len(nums)+2):
            if i not in nums:
                ans = min(ans, i)
        return ans
    
#         n = len(nums)
#         for i in range(n):
#             while nums[i]-1 in range(n) and nums[i] != nums[nums[i]-1]:
#                 nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                
#         return ([i == nums[i]-1 for i in range(n)] + [0]).index(False) + 1  