'''
Given a positive integer, output its complement number. 
The complement strategy is to flip the bits of its binary representation.
'''

# SOLUTION

def findComplement(num):
    X = 1
    
    while num > X:
        X = X * 2 + 1
        
    return X - num

# the way to think for this program is "num" + "num compliment" = 111....11 => let it be X
# the edge case is only zero

'''
N + bitwiseComplement(N) = 11....11 = X
Then bitwiseComplement(N) = X - N

O(logN) Time
O(1) Space
'''