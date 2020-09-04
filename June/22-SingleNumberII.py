"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

# SOLUTION

def singleNumber(self, nums: List[int]) -> int:
    P = (sum(nums) - sum(set(nums)))//2
    return sum(nums)-3*P

# arithemetic solution for this case, i do not know if the set counts as O(1) space,

"""
    single = 0
    for i in range(32):
        count = 0
        for num in nums:
            if num & (1<<i) == (1<<i): count += 1
        single |= (count%3) << i
        
    return single if single < (1<<31) else single - (1<<32) 
"""

# bitwise solution which most companies look for in such a question.