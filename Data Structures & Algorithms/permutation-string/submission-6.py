class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = Counter(s1)
        i = 0
        while i < len(s2)-len(s1)+1:
            if not s2[i] in freq:
                i += 1
                continue
            dupFreq = dict(freq)
            res = True
            print(i)
            for j in range(i, i+len(s1)):
                if not s2[j] in dupFreq:
                    i = j
                    res = False
                    break
                if dupFreq[s2[j]] <= 0:
                    res = False
                    break
                dupFreq[s2[j]] -= 1
                print(dupFreq)
            if res:
                return res
            i += 1
        return False
