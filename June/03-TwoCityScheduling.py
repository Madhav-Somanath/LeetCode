"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0],
and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
"""

# SOLUTION

def twoCitySchedCost(costs: List[List[int]]) -> int:
    
    costs.sort(key = lambda C: C[0] - C[1])
    A = sum([cost[0] for cost in costs[:len(costs) // 2]])
    B = sum([cost[1] for cost in costs[len(costs) // 2:]])
    return A + B

# here a greedy approach is considered 
