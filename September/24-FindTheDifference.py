""" Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t. """

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''XOR with sum of both strings'''
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)
        
        '''Difference approach'''
        # diff = 0
        # for i in range(len(s)):
        #     diff -= ord(s[i])
        #     diff += ord(t[i])
        # diff += ord(t[-1])
        # return chr(diff)

        '''Dictionary approach classical'''
        # dic = {}
        # for ch in s:
        #     dic[ch] = dic.get(ch, 0) + 1
        # for ch in t:
        #     if dic.get(ch, 0) == 0:
        #         return ch
        #     else:
        #         dic[ch] -= 1
        