""" Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times. """

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res, n = [], newInterval
        
        for index, i in enumerate(intervals):
            if i[1] < n[0]:
                res.append(i)
                
            elif n[1] < i[0]:
                res.append(n)
                return res + intervals[index:]
            
            else:  # overlap case
                n[0] = min(n[0], i[0])
                n[1] = max(n[1], i[1])
                
        res.append(n)
        return res
        
        
        '''
        intervals.append(newInterval)
        res = []
        for i in sorted(intervals, key=lambda x:x[0]):
            if res and res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res
        '''