class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not (s[left].isalpha() or s[left].isnumeric()):
                left += 1
            while right > left and not (s[right].isalpha() or s[right].isnumeric()):
                right -= 1
            if left >= right:
                return True
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True