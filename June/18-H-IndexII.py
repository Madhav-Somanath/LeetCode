"""
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
"A scientist has index h if h of his/her N papers have at least h citations each,
and the other N − h papers have no more than h citations each."
"""

# SOLUTION

def hIndex(self, citations: List[int]) -> int:
    n = len(citations)
    l, r = 0, n-1
    while l <= r:
        mid = (l+r)//2
        if citations[mid] >= n-mid:
            r = mid - 1
        else:
            l = mid + 1
    return n-l

# Unnecessarily confusing question for a basic binary search