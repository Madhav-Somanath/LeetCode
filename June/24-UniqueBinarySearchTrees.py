"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""

# SOLUTION

def numTrees(n: int) -> int:
    
    numTree = [1] * (n + 1)
    
    for nodes in range(2, n + 1):
        total = 0
        
        for root in range(1, nodes + 1):
            left = root - 1
            right = nodes - root
            total += numTree[left] * numTree[right]
            
        numTree[nodes] = total
        
    return numTree[n]

'''
math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))
'''