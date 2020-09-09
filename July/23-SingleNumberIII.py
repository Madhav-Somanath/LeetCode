""" Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once. """

# SOLUTION

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        a = 0
        b = 0
        for num in nums:
            xor ^= num
        mask = 1
        while(xor&mask == 0):
            mask = mask << 1
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
    
'''  

The binary mask has only one digit equals to one (in this case, mask = 2 = 0010)
xor = 3^5 = 6 = 0110.
for all numbers in nums other than 3, 5, each pair will counteract themselves no matter this pair belongs to 'num&mask ==0' or 'num&mask !=0', what you wanna do is put 3 and 5 into these two different statements, respectively.
thus, for xor = 0110, each '1' digit comes from 3 (0011) or 5 (0101) according to the property of operator '^'.
based on the while loop, xor&mask != 0 means there is only one common digit of both xor and mask that equals to 1 (xor = 0110, mask = 0010) and this '1' digit either comes from 3 or 5.
Thus, 3&mask and 5&mask must have different results (0011&0010 = 0010, 0101&0010 = 0000), which means 'a ^=num' won't contain both the cases of (num=3, num=5).
based on the steps above, the 3 and 5 will be sure to be assigned to a and b, respectively.

'''