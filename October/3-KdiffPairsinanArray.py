""" Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

    0 <= i, j < nums.length
    i != j
    a <= b
    b - a == k """

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        if k > 0:
            res = sum([i + k in count for i in count])
        else:
            res = sum([count[i] > 1 for i in count])
        return res