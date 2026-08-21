class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= target < nums[mid] or (nums[l] > nums[mid] and (target < nums[mid] or target >= nums[l])):
                r = mid - 1
            else:
                l = mid + 1
        return -1
