""" Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
"""

# SOLUTION

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        diff = [prices[i+1] - prices[i] for i in range(n-1)]
        dp, dp_max = [0]*(n + 1), [0]*(n + 1)
        for i in range(n-1):
            dp[i] = diff[i] + max(dp_max[i-3], dp[i-1])
            dp_max[i] = max(dp_max[i-1], dp[i])
            
        return dp_max[-3]
    
'''
For all this buy and sell stocks problems I prefer to use differences array. For example, if you have [1,2,3,1,4], then we have [1, 1, -2, 3] differences. Then the goal is to take as many of subarrays (with adjacent elements) with biggest sum, such that there is not gap with size 1. For example, for given differences, we can not take [1,1] and [3], but we can take [1] and [3], so the answer will be 4.

Let n be number of elements in prices, than there will be n-1 elements in diff array. Let us create dp and dp_max arrays with n+1 elements, that is two extra elements, such that

    dp[i] is maximum gain for first i elements of diff, where we use i-th element
    dp_max[i] is maximum gain for first i elements of diff (we can use i and we can not use it).

Now, we can do the following steps:

    dp[i] = diff[i] + max(dp_max[i-3], dp[i-1]), because, first of all we need to use i, so we take diff[i]. Now we have two options: skip 2 elements and take dp_max[i-3], or do not skip anything and take dp[i-1].
    Update dp_max[i] = max(dp_max[i-1], dp[i]), standard way to update maximum.
    Finally, we added 2 extra elements to dp and dp_max, so instead of dp_max[-1] we need to return dp_max[-3].

Complexity: both time and space complexity is O(n). Space complexity can be improved to O(1), because we look only 3 elements to the back.
'''

# def maxProfit(self, prices):
#     notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
#     for p in prices:
#         hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
#     return max(notHold, notHold_cooldown)