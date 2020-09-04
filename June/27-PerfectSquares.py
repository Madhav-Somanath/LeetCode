"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
"""

# SOLUTION

def numSquares(n: int) -> int:
        
    squares = [i**2 for i in range(1, int(n**0.5)+1)]
    
    d, q, nq = 1, {n}, set()
    
    while q:
        for node in q:
            for square in squares:
                if node == square:
                    return d
                if node < square:
                    break
                nq.add(node-square)
                
        q, nq, d = nq, set(), d+1
        
"""
The root node is n, and we are trying to keep reduce a perfect square number from it each layer.
So the next layer nodes are {n - i**2 for i in range(1, int(n**0.5)+1)}. And target leaf node is 0,
indicates n is made up of a number of perfect square numbers and depth is the least number of perfect square numbers.

Each while loop takes Si, which is the number of the values that is within range {1, n} whose least number of perfect squares is i.
E.g. S1 = √n. So total time cost should be c∑Si = cS1+cS2+...+cSd.
Since I used a set for queue here, ∑Si ≤ n, and time complexity is O(n).
The worst case would be n happen to have a larger least number of perfect square than any number from {1, n-1}.
"""