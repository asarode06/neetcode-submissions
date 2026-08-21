class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + "#" + s)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        adding = False
        length = ""
        intLength = 0
        for char in s:
            if adding:
                if intLength != 0:
                    res[-1] += char
                    intLength -= 1
                    continue
                else:
                    adding = False
                    length = ""
                
            if char == "#":
                intLength = int(length)
                adding = True
                res.append("")
            else:
                length += char
        return res
