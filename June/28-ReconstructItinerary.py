"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. 
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. 
    - For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.
    One must use all the tickets once and only once.
"""

# SOLUTION

import collections
def findItinerary(tickets: List[List[str]]) -> List[str]:
    targets = collections.defaultdict(list)
    #defaultfict here to handle key errors
    
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b, #comma at the end to ensure its list appended
        
    route = []
    
    def visit(airport):
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)

    visit('JFK')
    return route[::-1]