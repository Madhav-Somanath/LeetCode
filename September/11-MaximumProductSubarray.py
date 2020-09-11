""" Given an integer array nums, find the contiguous subarray
within an array (containing at least one number) which has the largest product. """

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(nums + B)
    
'''
N = len(nums)
dp1 = [0] * N
dp2 = [0] * N
dp1[0] = dp2[0] = nums[0]

for k in range(1, N):
    if nums[k] > 0:
        dp1[k] = max(dp1[k-1] * nums[k], nums[k])
        dp2[k] = dp2[k-1] * nums[k]
    else:
        dp1[k] = dp2[k-1] * nums[k]
        dp2[k] = min(dp1[k-1] * nums[k], nums[k])

return max(dp1)
'''