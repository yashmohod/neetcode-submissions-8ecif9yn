class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        rec = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in rec:
                return [rec[dif],i]
            else:
                rec[nums[i]]= i