from heapq import heapify,heappop,heappush
def lastStoneWeight(stones):
    h = [-x for x in stones]
    heapify(h)
    while len(h) > 1:
        heappush(h, heappop(h) - heappop(h))
    return -h[0]