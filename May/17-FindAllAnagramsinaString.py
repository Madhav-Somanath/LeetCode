"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""

# SOLUTION

from collections import defaultdict

def findAnagrams(s, p):
    if len(s) < len(p) : 
        return []
    
    res = []
    pDict = defaultdict(int)
    sDict = defaultdict(int)

    for i in p :
        pDict[i] += 1
        
    for i in s[:len(p)-1] :
        sDict[i] += 1
    
    for i in range(len(p)-1, len(s)) : 
        sDict[s[i]] += 1
        if sDict == pDict : 
            res.append(i-len(p)+1)
        sDict[s[i-len(p)+1]] -= 1
        if sDict[s[i-len(p)+1]] == 0 : 
            del sDict[s[i-len(p)+1]]
        
    return res

# i prefer using "Counter" from collections but sadly it takes longer to process,
# so this solution provided by another user on leetcode is my preffered method or solving this question