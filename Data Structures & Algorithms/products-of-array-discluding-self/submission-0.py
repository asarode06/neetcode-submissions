class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0]*len(nums)
        post = [0]*len(nums)
        res = [0]*len(nums)

        pre[0] = post[-1] = 1

        for n in range(1, len(nums)):
            pre[n] = pre[n-1]*nums[n-1]
        for n in range(len(nums)-2, -1, -1):
            post[n] = post[n+1]*nums[n+1]
        for n in range(len(nums)):
            res[n] = pre[n]*post[n]
        return res