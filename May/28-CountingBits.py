"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num 
calculate the number of 1's in their binary representation and return them as an array.
"""

# SOLUTION

def countBits(self, num: int) -> List[int]:
    
    res = [0]
    
    while len(res) <= num:
        res += [i+1 for i in res]
        
    return res[:num+1]

# Magic loops *wink wink*