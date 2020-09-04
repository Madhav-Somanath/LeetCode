def maxSubArray(nums):
    
    maxsum = nums[0]
    currentsum = nums[0]

    for i in range(1, len(nums)):
        
        currentsum = max(nums[i], currentsum + nums[i])
        maxsum = max(currentsum, maxsum)
        
    return maxsum