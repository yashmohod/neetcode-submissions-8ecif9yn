class Solution:
    def canJump(self, nums: List[int]) -> bool:
        g = len(nums)-1

        for i in range(len(nums)-1,-1,-1):

            if g-i <= nums[i]:
                g =i
        
        return g == 0