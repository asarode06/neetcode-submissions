class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        min = prices[0]
        maxSell = 0
        for n in range(1, len(prices)):
            if prices[n] - min > maxSell:
                maxSell = prices[n] - min
            if prices[n] < min:
                min = prices[n]
        return maxSell