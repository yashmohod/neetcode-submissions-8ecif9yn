class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g = len(nums)-1
        i = g-1
        while i > -1:
            if g-i <= nums[i]:
                g =i
            i-=1        
        
        return g == 0