""" You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips.  """

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        stops = [0] * 1001
        
        for n, i, j in trips:
            stops[i] += n
            stops[j] -= n
            
        for v in stops:    
            capacity -= v
            
            if capacity < 0:
                return False
            
        return True
        
    '''O(n or 1001) for this method and O(nlogN) time and O(N) space for secondary'''
        
    # heap = []

    # for n, i, j in trips:
    #     heapq.heappush(heap, (j, -n))
    #     heapq.heappush(heap, (i, n))
        
    # while heap:
    #     capacity -= heapq.heappop(heap)[1]    
        
    #     if capacity < 0:
    #         return False

    # return True
    
    