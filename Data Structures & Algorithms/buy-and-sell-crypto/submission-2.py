class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min_cost
            min_cost = min(min_cost, prices[i])
            max_profit = max(max_profit, profit)
        return max_profit