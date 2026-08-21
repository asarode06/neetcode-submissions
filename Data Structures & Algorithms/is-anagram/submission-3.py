class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = [0] * 26
        tMap = [0] * 26
        for i in range(len(s)):
            sMap[ord(s[i]) - 97] += 1
            tMap[ord(t[i]) - 97] += 1
        
        for i in range(26):
            if sMap[i] != tMap[i]:
                return False
        return True

