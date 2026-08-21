from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0,1
        charMap = defaultdict(int)
        maxSub = 0
        maxF = 0
        while j <= len(s):
            charMap[s[j-1:j]] += 1
            maxF = max(maxF, charMap[s[j-1:j]])
            while j - i - maxF > k:
                charMap[s[i: i+1]] -= 1
                i += 1
            maxSub = max(maxSub, j-i)
            j += 1
        return maxSub
            
