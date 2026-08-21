class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        minVal = prices[0]
        maxSell = 0
        for n in range(1, len(prices)):
            if prices[n] - minVal > maxSell:
                maxSell = prices[n] - minVal
            if prices[n] < minVal:
                minVal = prices[n]
        return maxSell