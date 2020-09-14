""" You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police. """

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = curr = 0
        for num in nums:
            temp = prev # This represents the nums[i-2]th value
            prev = curr # This represents the nums[i-1]th value
            curr = max(num + temp, prev) # Here we just plug into the formula
        return curr
    
'''
https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
'''