def maximalSquare(self, matrix: List[List[str]]) -> int:
    
    if not matrix:
        return 0
    m , n = len(matrix),len(matrix[0])
    dp = [[0 if matrix[i][j]=='0' else 1 for j in range(n)]for i in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j] =='1':
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            else:
                dp[i][j] = 0

    ans = max([max(i) for i in dp])
    return ans ** 2
'''
We define dp[i][j] the maximal ending at position (i, j). Thus, current state (dp[i][j])depends on left (dp[i][j - 1]), up (dp[i - 1][j]), and left-up's (dp[i - 1][j - 1]) states. The current state equals to the minimum of these three states plus matrix[i][j] because any smaller value will lead to a smaller square (holes in somewhere). I use maxArea to track the maximal square. When matrix[i][j] == '0', the maximal square ending at position (i, j) is obviously 0.

Recurrence relation:

For matrix[i][j] == 1, dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + int(matrix[i][j]).

For matrix[i][j] == 0, dp[i][j] = 0
'''