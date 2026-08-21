class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        
        while l <= r:
            midRow = int(int((l+r) / 2) / len(matrix[0]))
            midCol = int((l+r) / 2) % len(matrix[0])
            if matrix[midRow][midCol] > target:
                r = int((l+r) / 2) - 1
            elif matrix[midRow][midCol] < target:
                l = int((l+r) / 2) + 1
            else:
                return True
        return False