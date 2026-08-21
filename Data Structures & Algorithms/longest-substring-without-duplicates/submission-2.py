class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        longest = 1
        l, r = 0, 1
        charSet = set()
        charSet.add(s[0])
        while r < len(s):
            if s[r] in charSet:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(s[r])
            r += 1
            longest = max(longest, r-l)
        return longest
            