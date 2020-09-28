""" Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k. """

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, prod, count = 0, 1, 0
            
        for right in range(len(nums)):
            prod *= nums[right]            

            while prod >= k and left <= right:                    
                prod /= nums[left]
                left += 1                        
            count += right - left + 1                
        return count