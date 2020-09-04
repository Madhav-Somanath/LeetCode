'''
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once.
Find this single element that appears only once.
'''

# SOLUTION

def singleNonDuplicate(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] == nums[mid ^ 1]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]

# all credits to Stefan Pochmann :)
    