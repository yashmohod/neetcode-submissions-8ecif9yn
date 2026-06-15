class Solution:
    def rob(self, nums: List[int]) -> int:
        l,r = 0,0
        for i in nums[:-1]:
            l,r = r,max(r,l+i)
        
        l2,r2 = 0,0
        for i in nums[1:]:
            l2,r2 = r2,max(r2,l2+i)
        return max(nums[0],r,r2)