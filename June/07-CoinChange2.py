"""
You are given coins of different denominations and a total amount of money.

Write a function to compute the number of combinations that make up that amount.

You may assume that you have infinite number of each kind of coin.
"""

# SOLUTION

def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in coins:
        for j in range(1, amount + 1):
            if j >= i:
                dp[j] += dp[j - i]
    return dp[amount]

# classic DP program, DP array is taken as amount to make it number of combinations, otherwise it would be permutations.