class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}
        for sLetter, tLetter in zip(s, t):
            if sLetter in sMap:
                sMap[sLetter] += 1
            else:
                sMap[sLetter] = 0
            
            if tLetter in tMap:
                tMap[tLetter] += 1
            else:
                tMap[tLetter] = 0
        return sMap == tMap
            