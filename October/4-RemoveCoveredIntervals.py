""" Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals. """

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], -x[1]))
        
        right, rem, n = -1, 0, len(intervals)
        
        for start, end in intervals:
            
            if end <= right:
                rem += 1
            else:
                right = end
        return n - rem