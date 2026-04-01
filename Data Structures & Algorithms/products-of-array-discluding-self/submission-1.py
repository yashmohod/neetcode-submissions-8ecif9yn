class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)):
            res[len(nums)-i-1] *= postfix
            postfix *= nums[len(nums)-i-1]
        return res

        return []



        return res