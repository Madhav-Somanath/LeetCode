"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
"""

# SOLUTION

import heapq

def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    
    heap = []
    
    for point in points:
        dist = point[0] * point[0] + point[1] * point[1]
        heapq.heappush(heap, (-dist, point))
        
        if len(heap) > K:
            heapq.heappop(heap)

    return [tuple[1] for tuple in heap]

# return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)

# Min heap is used here with an easy alternative listed below