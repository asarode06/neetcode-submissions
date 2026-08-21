class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            target = -1*num
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

        return res