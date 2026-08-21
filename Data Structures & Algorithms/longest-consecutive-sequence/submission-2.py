class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            
            currNum = num + 1
            while currNum in numSet:
                currNum += 1
            
            maxLen = max(maxLen, currNum - num)

        return maxLen