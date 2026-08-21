class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low <= high:
            mid = int((low+high)/2)
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/mid)
            if hrs <= h:
                high = mid - 1
                res = mid
            else:
                low = mid + 1
        return res
