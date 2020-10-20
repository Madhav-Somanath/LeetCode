""" In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1. """

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for x in [A[0],B[0]]:
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1
    
    '''
    # Intersection method
    
    s = reduce(set.__and__, (set(d) for d in zip(A, B)))
    if not s: return -1
    x = s.pop()
    return min(len(A) - A.count(x), len(B) - B.count(x))
    
    
    # Expanded method No:1
    
    if len(A) != len(B): return -1
    same, countA, countB = Counter(), Counter(A), Counter(B)
    for a, b in zip(A, B):
        if a == b:
            same[a] += 1
    for i in range(1, 7):
        if countA[i] + countB[i] - same[i] == len(A):
            return min(countA[i], countB[i]) - same[i]        
    return -1
    '''