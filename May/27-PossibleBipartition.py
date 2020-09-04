"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.
"""

# SOLUTION
 
def possibleBipartition(N: int, dislikes: List[List[int]]) -> bool:
    
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for a,b in dislikes:
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    group = defaultdict(int)

    for i in range(1, N+1):
        if i not in group:
            q.append(i)
            group[i] = 1
            
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in group:
                    group[nei] = -group[node]
                    q.append(nei)
                elif nei in group and group[nei] != -group[node]:
                    return False

    return True