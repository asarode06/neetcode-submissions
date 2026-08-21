class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            freq = [0] * 26
            for letter in word:
                index = ord(letter) - 97
                freq[index] += 1
            tupFreq = tuple(freq)
            if tupFreq in groups:
                groups[tupFreq].append(word)
            else:
                groups[tupFreq] = [word]
        res = []
        for val in groups.values():
            res.append(val)
        return res