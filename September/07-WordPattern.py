""" Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str. """

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        x = str.split(' ')
        lsp = len(set(pattern))
        lsx = len(set(x))
        return len(x)==len(pattern) and lsx==lsp and lsp== len(set(zip(pattern, x)))