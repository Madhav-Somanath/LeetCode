"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
and you want to check one by one to see if T has its subsequence.
In this scenario, how would you change your code?

"""

# SOLUTION

def isSubsequence(s: str, t: str) -> bool:
    for c in s:
        i = t.find(c)
        if i == -1:
            return False
        else:
            t = t[i+1:]
    return True

'''
remainder_of_t = iter(t)
for letter in s:
    if letter not in remainder_of_t:
        return False
return True

t = iter(t)
return all(c in t for c in s)
'''

# i do not know how to answer the follow up, if anyone could help me it would be great :)
# also the approach here is to use iter to only see through forward iterations

# time space complexity : time = O(s*t) space = O(t)
# added solution complexity: time = O(s+t) space = O(1)
