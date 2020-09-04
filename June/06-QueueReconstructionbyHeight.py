"""
Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k), where h is the height of the person,
and k is the number of people in front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
"""

# SOLUTION

def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    people.sort(key = lambda x: [-x[0],x[1]])
    
    res = []
    for p in people:
        res.insert(p[1], p)
    return res

# simple use of sorting using lambda key and inserting into position afterwards to keep sort integrity