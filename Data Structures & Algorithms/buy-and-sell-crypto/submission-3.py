class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0
        for sell in prices[1:]:
            maxProfit = max(maxProfit, sell - minBuy)
            minBuy = min(sell, minBuy)
            
        return maxProfit