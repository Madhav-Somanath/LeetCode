""" On a 2-dimensional grid, there are 4 types of squares:

    1 represents the starting square.  There is exactly one starting square.
    2 represents the ending square.  There is exactly one ending square.
    0 represents empty squares we can walk over.
    -1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square,
that walk over every non-obstacle square exactly once. """

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        self.res = 0
        m, n, empty = len(grid), len(grid[0]), 1
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    x, y = (i, j)
                elif grid[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0):
                return
            
            if grid[x][y] == 2:
                self.res += empty == 0
                return
            
            grid[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            grid[x][y] = 0
            
        dfs(x, y, empty)
        return self.res
    
'''
First find out where the start and the end is.
Also We need to know the number of empty cells.

We we try to explore a cell,
it will change 0 to -2 and do a dfs in 4 direction.

If we hit the target and pass all empty cells, increment the result.
'''