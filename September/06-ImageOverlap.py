""" Two images A and B are given, represented as binary, square matrices of the same size.  
(A binary matrix has only 0s and 1s as values.)
We translate one image however we choose (sliding it left, right, up, or down any number of units), 
and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap? """

import numpy as np
from collections import Counter, defaultdict

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        '''Flatten the matrix and count distance values for optimization: O(N^2) => O(AB) => O(AB + N^2)'''
        A = [(i, j) for i, row in enumerate(A) for j, item in enumerate(row) if item]
        B = [(i, j) for i, row in enumerate(B) for j, item in enumerate(row) if item]
        count = Counter((ax-bx, ay-by) for ax, ay in A for bx, by in B)
        return max(count.values() or [0])
        
        '''Count 1's take distance, translation values determine maximum overlap: O(N^4) (2N, 2N sliding)''' 
        # d = defaultdict(int)
        # a = []
        # b = []
        # for i in range(len(A)):
        #     for j in range(len(A[0])):
        #         if(A[i][j] == 1):
        #             a.append((i,j))
        #         if(B[i][j] == 1):
        #             b.append((i,j))
        # ans = 0
        # for t1 in a:
        #     for t2 in b:
        #         t3 = (t2[0]-t1[0],t2[1]-t1[1])
        #         d[t3] += 1
        #         ans = max(ans, d[t3]) # is this really different?
        # return ans
        
        '''Fast fourier transform method: O(N^2 log N)'''

        # n = len(A)
        # A1 = np.pad(A, [(0, n), (0, n)], mode='constant', constant_values=0)
        # B1 = np.pad(B, [(0, n), (0, n)], mode='constant', constant_values=0)
        # A2 = np.fft.fft2(A1)
        # B2 = np.fft.ifft2(B1)
        # return int(np.round(np.max(np.abs(np.fft.fft2(A2 * B2)))))