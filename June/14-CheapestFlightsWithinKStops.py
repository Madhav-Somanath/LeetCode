"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst,
your task is to find the cheapest price from src to dst with up to k stops.
If there is no such route, output -1.

Constraints:

    The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
    The size of flights will be in range [0, n * (n - 1) / 2].
    The format of each flight will be (src, dst, price).
    The price of each flight will be in the range [1, 10000].
    k is in the range of [0, n - 1].
    There will not be any duplicated flights or self cycles.
"""
 
# SOLUTION

from collections import defaultdict
from heapq import heappop, heappush

def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    f = defaultdict(dict)
    for a, b, p in flights:
        f[a][b] = p
    heap = [(0, src, K + 1)]
    while heap:
        p, i, k = heappop(heap)
        if i == dst:
            return p
        if k > 0:
            for j in f[i]:
                heappush(heap, (p + f[i][j], j, k - 1))
    return -1

# Very good graph problem, self explainatory solution