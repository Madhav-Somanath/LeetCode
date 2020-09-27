""" You are given equations in the format A / B = k, where A and B are variables represented as strings,
and k is a real number (floating-point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction. """

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for ([x,y],value) in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1/value
        
        def find_prod(s,e):
            if s not in graph or e not in graph:
                return -1.0
            if s==e: return 1.0
            q = deque([(s, 1.0)])
            visited = {s}
            while q:
                n, curr = q.popleft()
                for child,value in graph[n].items():
                    if child in visited:
                        continue
                    nc = curr*value
                    if child == e:
                        return nc
                    graph[s][child] = nc
                    graph[child][s] = 1/nc
                    visited.add(child)
                    q.append((child, nc))
            return -1.0
        
        return [find_prod(s,e) for [s,e] in queries]

    '''
        quot = collections.defaultdict(dict)
    for (num, den), val in zip(equations, values):
        quot[num][num] = quot[den][den] = 1.0
        quot[num][den] = val
        quot[den][num] = 1 / val
    for k, i, j in itertools.permutations(quot, 3):
        if k in quot[i] and j in quot[k]:
            quot[i][j] = quot[i][k] * quot[k][j]
    return [quot[num].get(den, -1.0) for num, den in queries]
    '''