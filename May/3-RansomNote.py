'''
 Given an arbitrary ransom note string and another string containing letters from all the magazines, 
 write a function that will return true if the ransom note can be constructed from the magazines; 
 otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note. 
'''

# SOLUTION

import collections

def canConstruct(ransomNote, magazine):
    count = collections.Counter(magazine)
    
    for ch in ransomNote:
        if ch in count and count[ch] > 0:
            count[ch] -= 1
        else:
            return False
        
    return True

# space efficient way is to not follow this dictionary route, but it works :D