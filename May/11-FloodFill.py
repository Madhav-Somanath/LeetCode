'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill": 
    consider the starting pixel,
    plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
    plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.
Replace the color of all of the aforementioned pixels with the newColor.
At the end, return the modified image.
'''

# SOLUTION

def floodFill(image, sr, sc, newColor):
    def dfs(i, j):
        image[i][j] = newColor
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < m and 0 <= y < n and image[x][y] == old:
                dfs(x, y)
    old, m, n = image[sr][sc], len(image), len(image[0])
    if old != newColor: 
        dfs(sr, sc)
    return image
    
    '''
    old, m, n = image[sr][sc], len(image), len(image[0])
    if old != newColor: 
        q = collections.deque([(sr, sc)])
        while q:
            i, j = q.popleft()
            image[i][j] = newColor
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                    q.append((x, y))
    return image
    '''

# classif dfs solution, ive also included a bfs solution here which i found from the discussion tab