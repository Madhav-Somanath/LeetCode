"""
Given a set of distinct positive integers, find the largest subset such that
every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
"""

# SOLUTION

def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
            
        if not nums:
            return nums
        nums.sort()
        
        dp = [1 for i in range(len(nums))]
        res = []
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        for i in range(1, max(dp) + 1):
            res.append(nums[dp.index(i)])
        return res
    
'''
dp = [[]]
for n in sorted(nums):
    dp.append([n] + max((s for s in dp if not s or n % s[0] == 0), key=len))
return max(dp, key=len)
'''

# to he honest i cant wrap my head around this solution, thank you to the legends Stefan and Shenggu for this solution