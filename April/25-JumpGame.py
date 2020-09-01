def canJump(nums):
    
    lastPos = len(nums) - 1
    
    for  i in range(len(nums)-1,  -1, -1):
        
        if i + nums[i] >= lastPos:
            lastPos = i
            
    return lastPos == 0