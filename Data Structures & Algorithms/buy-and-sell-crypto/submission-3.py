class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
            minPrice = min(minPrice, prices[i])
        return maxProfit