""" Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome. """

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(ch for ch in s if ch.isalnum()).lower()
        return res == res[::-1]