""" Given an array of integers A, We need to sort the array performing a series of pancake flips.

In one pancake flip we do the following steps:

    Choose an integer k where 0 <= k < A.length.
    Reverse the sub-array A[0...k].

For example, if A = [3,2,1,4] and we performed a pancake flip choosing k = 2, we reverse the sub-array [3,2,1],
so A = [1,2,3,4] after the pancake flip at k = 2.

Return an array of the k-values of the pancake flips that should be performed in order to sort A.
Any valid answer that sorts the array within 10 * A.length flips will be judged as correct. """

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        res = []
        for i in range(n):
            cur_max = max(A[0:n-i])
            j = 0
            while A[j] != cur_max:
                j += 1

            A[:j+1] = reversed(A[:j+1])
            res.append(j+1)

            A[:n-i] = reversed(A[:n-i])
            res.append(n-i)
        return res