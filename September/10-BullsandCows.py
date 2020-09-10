""" You are playing the following Bulls and Cows game with your friend:
You write down a number and ask your friend to guess what the number is.
Each time your friend makes a guess, you provide a hint that indicates
how many digits in said guess match your secret number exactly in both digit and position
(called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows").
Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess,
use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits. """

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        B = sum([x==y for x,y in zip(secret, guess)])
        
        Count_sec = Counter(secret)
        Count_gue = Counter(guess)
        
        B_C = sum([min(Count_sec[elem], Count_gue[elem]) for elem in Count_sec])
        
        return str(B) + "A" + str(B_C-B) + "B"
    
'''

Let us first evaluate number of bulls B: by definition it is number of places with the same digit in secret and guess: so let us just traverse our strings and count it.

Now, let us evaluate both number of cows and bulls: B_C: we need to count each digit in secret and in guess and choose the smallest of these two numbers. Evaluate sum for each digit.

Finally, number of cows will be B_C - B, so we just return return the answer!

Complexity: both time and space complexity is O(1). Imagine, that we have not 4 lengths, but n, then we have O(n) time complexity and O(10) space complexity to keep our counters.

'''