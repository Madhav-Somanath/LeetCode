""" All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T',
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. """

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = collections.Counter(s[i:i+10] for i in range(0, len(s) - 9))
        return [key for key in counter if counter[key] > 1]