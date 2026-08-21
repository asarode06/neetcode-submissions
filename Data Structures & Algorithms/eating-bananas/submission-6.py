class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate, maxRate = 1, max(piles)
        resRate = 1

        while minRate <= maxRate:
            rate = (minRate + maxRate) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / rate)
            
            if time <= h:
                resRate = rate
                maxRate = rate - 1
            else:
                minRate = rate + 1
        return resRate