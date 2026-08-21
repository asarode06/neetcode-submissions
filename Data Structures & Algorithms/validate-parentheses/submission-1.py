class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter in '}])':
                if len(stack) == 0:
                    return False
                comb = stack.pop()+letter
                if comb != '{}' and comb != '[]' and comb != '()':
                    return False
            else:
                stack.append(letter)
        return len(stack) == 0

