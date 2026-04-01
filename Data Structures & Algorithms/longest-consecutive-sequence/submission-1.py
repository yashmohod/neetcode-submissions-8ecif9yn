class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(list(set(nums)))
        l = 0
        res = 1

        while l < len(nums)-1:
            r = l
            while r + 1 < len(nums) and nums[r+1] == nums[r] + 1:
                r+=1
            res = max(res, r-l + 1)
            l = r + 1
        
        return res