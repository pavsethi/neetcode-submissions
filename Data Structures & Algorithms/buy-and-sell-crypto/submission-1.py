class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = prices[0]
        for sell in prices:
            maxP = max(maxP, sell - buy)
            buy = min(buy, sell)
        return maxP