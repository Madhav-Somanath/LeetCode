""" Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally. """

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))
        return dp[-1]
    
    '''
    @lru_cache(None)
    def dfs(state):
        if state == 0: return False
        for i in range(1, int(math.sqrt(state))+1):
            if not dfs(state - i*i): return True
        return False

    return dfs(n)
    '''