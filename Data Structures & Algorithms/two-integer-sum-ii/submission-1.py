class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            sumNums = numbers[i] + numbers[j]
            if sumNums < target:
                i += 1
            elif sumNums > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return [0, 0]
        