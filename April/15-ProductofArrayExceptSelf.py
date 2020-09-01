def productExceptSelf(nums):
    if len(nums) == 0:
        return [0]
    n = len(nums)
    temp = 1
    prod = [1] * n
    
    for i in range(n):
        prod[i] = temp
        temp *= nums[i]
        
    temp = 1

    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= nums[i]

    return prod