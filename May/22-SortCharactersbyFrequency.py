"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""

# SOLUTION

from collections import Counter
def frequencySort(self, s: str) -> str:
    return "".join(char * times for char, times in Counter(s).most_common())

# Probably the best way ive used Counter concepts.