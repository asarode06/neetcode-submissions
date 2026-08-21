class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for letter in s:
            if letter in pairs:
                if not stack or stack.pop() != pairs[letter]:
                    return False
            else:
                stack.append(letter)

        return not stack

