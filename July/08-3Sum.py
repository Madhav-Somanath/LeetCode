""" Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero. """

# SOLUTION

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N, result = len(nums), []
        
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            target = nums[i]*-1
            s,e = i+1, N-1
            
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]: #edge
                        s = s+1
                        
                elif nums[s] + nums[e] < target:
                    s = s+1
                    
                else:
                    e = e-1
                    
        return result
    
# converted 3 sum into 2 sum and solved edge cause for possible repeated triplets at "edge" marker