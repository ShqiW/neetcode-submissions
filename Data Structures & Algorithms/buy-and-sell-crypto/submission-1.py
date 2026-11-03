class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = prices[0]
        profit = 0
        for p in prices:
            
            profit = max(profit, p - min_cost)
            min_cost = min(min_cost, p)
        return profit        