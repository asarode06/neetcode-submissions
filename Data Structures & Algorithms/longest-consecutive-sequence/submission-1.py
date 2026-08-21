class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for num in numSet:
            if (num - 1) in numSet:
                continue
            seqLen = 1
            while num + seqLen in numSet:
                seqLen += 1
            maxLen = max(seqLen, maxLen)
        return maxLen
