from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0,1
        charMap = defaultdict(int)
        maxSub = 0
        while j <= len(s):
            charMap[s[j-1:j]] += 1
            maxL = (0, '')
            for key in charMap:
                maxL = max((charMap[key], key), maxL)
            print(maxL)
            while j - i - maxL[0] > k:
                charMap[s[i: i+1]] -= 1
                print(charMap, s[i:j], s[i:i+1], i)
                if maxL[1] == s[i:i+1]:
                    maxL = (0, '')
                    for key in charMap:
                        maxL = max((charMap[key], key), maxL)
                    print(maxL)
                i += 1
            maxSub = max(maxSub, j-i)
            j += 1
        return maxSub
            
