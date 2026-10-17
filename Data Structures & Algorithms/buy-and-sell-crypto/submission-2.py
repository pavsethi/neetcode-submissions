class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = 10000000000
        maxProfit = 0
        for sell in prices:
            minBuy = min(sell, minBuy)
            maxProfit = max(maxProfit, sell - minBuy)
        return maxProfit