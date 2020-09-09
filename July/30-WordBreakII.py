""" Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words. """
    
# SOLUTION

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        def dfs(i): # return all possibilities in s[i:]
            
            if i in memo:
                return memo[i]
            
            else:
                res = []
                for word in wordDict:
                    
                    if i + len(word) == len(s) and word == s[i:i+len(word)]: # reaching the end
                        res.append(word)
                        
                    if i + len(word) < len(s) and word == s[i:i+len(word)]:
                        following_res = dfs(i + len(word)) # getting the suffix and add to the result
                        
                        for following in following_res:
                            res.append(word + " " + following)
                            
                memo[i] = res
                return res
        return dfs(0)