class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
             
        som = 0
        lg = nums[0]
        for r in range(len(nums)):
            if som < 0:
                som = 0
            som += nums[r]

            lg = max(lg,som)

        
        return lg