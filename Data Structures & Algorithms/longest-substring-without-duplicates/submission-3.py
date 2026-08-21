class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        maxLen = 0
        currChars = set()
        while r < len(s):
            if s[r] in currChars:
                while s[r] in currChars:
                    currChars.remove(s[l])
                    l += 1
            currChars.add(s[r])
            maxLen = max(maxLen, r-l+1)
            r += 1

        return maxLen