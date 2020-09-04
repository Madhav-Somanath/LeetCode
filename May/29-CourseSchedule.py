"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""

# SOLUTION

from collections import defaultdict

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    
    d = defaultdict(list)
    
    for u, v in prerequisites:
        d[u].append(v)
        
    visiting, visited = [False] * numCourses, [False] * numCourses
    
    def visit(u):
        visiting[u] = True
        ret = visited[u] or all(not visiting[v] and visit(v) for v in d[u])
        visiting[u] = False
        visited[u] = True
        return ret
    
    return all(visit(u) for u in range(numCourses))
