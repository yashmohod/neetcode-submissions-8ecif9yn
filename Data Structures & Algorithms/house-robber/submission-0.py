class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l,r = 0,0

        for i in nums:
            l,r = r,max(l+i,r)
        return max(l,r)