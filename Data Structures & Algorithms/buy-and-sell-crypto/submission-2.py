class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        maxVal, i, j = 0, 0, 1
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
            else:
                maxVal = max(maxVal, prices[j] - prices[i])
            j += 1
        return maxVal