class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        past = {}

        for i in range(len(nums)):

            dif = target - nums[i]

            if dif in past:
                return [past[dif],i]
            
            past[nums[i]] = i
        
