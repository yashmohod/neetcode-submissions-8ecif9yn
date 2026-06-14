class Solution:
    def rob(self, nums: List[int]) -> int:
        l,r = 0,0

        for i in nums:
            l,r = r,max(l+i,r)
        return r