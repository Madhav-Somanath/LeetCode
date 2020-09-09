""" Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.  """

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()
        
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
                
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)
    
'''
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)
    
    use = sum(v & ~1 for v in collections.Counter(s).values())
    return use + (use < len(s))
'''