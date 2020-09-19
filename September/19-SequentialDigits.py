""" An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits. """

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        ans = []
        for digit in range(1, 10):
            num = new = digit
            
            while num <= high and new < 10:
                if num >= low:
                    ans.append(num)
                    
                new += 1
                num = num * 10 + new
                
        return sorted(ans)