class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        currNums = set()
        for num in nums:
            if num in currNums:
                return True
            currNums.add(num)
        return False