class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0

        for i in range(len(nums)):
            res = res^nums[i]
            res = res^(i+1)
        return res
