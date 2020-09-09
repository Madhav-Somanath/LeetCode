""" Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0. """

# SOLUTION

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]
    
# time complexity O(n) space complexity O(a + b)?