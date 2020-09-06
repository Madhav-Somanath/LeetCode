""" Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string. """

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        for time in itertools.permutations(sorted(A, reverse=True)):
            if time[:2] < (2, 4) and time[2] < 6:
                return '%d%d:%d%d' % time
        return ''