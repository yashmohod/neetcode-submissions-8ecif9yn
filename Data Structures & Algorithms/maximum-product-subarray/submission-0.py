class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mm=1
        mn=1

        for i in nums:
            t = mm*i
            mm = max(t,mn*i,i)
            mn = min(t,mn*i,i)
            res = max(res,mm)
        return res






