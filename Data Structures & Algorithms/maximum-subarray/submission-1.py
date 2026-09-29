class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
             
        som = 0
        lg = -float("inf")
        l =0
        for r in range(len(nums)):
            som += nums[r]

            while l < len(nums) and som <=lg:
                som -=nums[l]
                l+=1
            lg = max(lg,som)

        
        return lg