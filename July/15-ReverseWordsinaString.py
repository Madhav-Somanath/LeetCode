""" Given an input string, reverse the string word by word. """

# SOLUTION

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
    
# they probably wouldnt ask this for python...