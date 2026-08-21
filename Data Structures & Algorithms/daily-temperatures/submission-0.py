class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        stack = []
        res = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                lesser = stack.pop()
                res[lesser[1]] = i - lesser[1]
            stack.append((temp, i))
        return res