'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1. 
'''

# SOLUTION
import collections
def firstUniqChar(s):
    
    count = collections.Counter(s)
    
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx     
    return -1

# Basic dictionary comprehension