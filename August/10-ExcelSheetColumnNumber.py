""" Given a column title as appear in an Excel sheet, return its corresponding column number. """

class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for exp, char in enumerate(reversed(s)):
            num += (ord(char) - ord('A') + 1) * (26 ** exp)
        return num