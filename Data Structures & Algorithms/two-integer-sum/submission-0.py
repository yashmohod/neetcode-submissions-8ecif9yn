class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx = {}

        for i in range(len(nums)):

            dif = target - nums[i]
            
            if dif in idx:
                return [idx[dif],i]
            
            idx[nums[i]] = i
