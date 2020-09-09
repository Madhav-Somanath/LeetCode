""" Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

    You may assume the interval's end point is always bigger than its start point.
    You may assume none of these intervals have the same start point. """


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        intvl = sorted([(x[0], i) for i, x in enumerate(intervals)], key=lambda x: x[0])
        
        starts, idx = [x[0] for x in intvl], [x[1] for x in intvl]
        
        res = []
        
        for x in intervals:
            pos = bisect.bisect_left(starts, x[1])
            if pos == len(starts):
                res.append(-1)
            else:
                res.append(idx[pos])
        return res

