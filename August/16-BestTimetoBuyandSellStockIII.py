""" Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again). """

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        one_buy = two_buy =   float('inf')
        one_profit = two_profit = 0
        
        for p in prices:
            
            one_buy = min(one_buy,p)
            one_profit = max(one_profit, p - one_buy)
            two_buy = min(two_buy, p - one_profit)
            two_profit = max(two_profit, p - two_buy)
            
        return two_profit