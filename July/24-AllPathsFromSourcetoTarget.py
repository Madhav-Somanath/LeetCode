""" Given a directed, acyclic graph of N nodes.
Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
graph[i] is a list of all nodes j for which the edge (i, j) exists. """

# SOLUTION

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph) - 1
        paths = [[0]]
        ans = []
        while paths:
            path = paths.pop()
            for n in graph[path[-1]]:
                if n == N:
                    ans.append(path + [n])
                else:
                    paths.append(path + [n])
        return ans
    
# im bad at graph questions but here the logic applies is that we keep creating the paths if they exis,
# and if it matches the length of the graph then we add it to the answer (?)