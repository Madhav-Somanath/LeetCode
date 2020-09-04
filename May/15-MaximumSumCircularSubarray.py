"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array. 
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once. 
(Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
"""

# SOLUTION

def maxSubarraySumCircular(A):
    
    if max(A) <= 0:
        return max(A)
    
    endmax = [i for i in A]
    endmin = [i for i in A]
    
    for i in range(1,len(A)):
        if endmax[i-1] > 0: endmax[i] += endmax[i-1]
        if endmin[i-1] < 0: endmin[i] += endmin[i-1]

    return max(max(endmax),sum(A) - min(endmin))

# Record all the max and min subarray sums that ends at index i.
# For non-circular sum, take the maximum of endmax; for circular sum, take sum(A)-min(endmin).