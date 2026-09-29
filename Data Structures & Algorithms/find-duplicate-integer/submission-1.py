class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        f,s = 0,len(nums)-1

        while f<len(nums) and s <len(nums):

            if  nums[s] == nums[f]:
                return nums[s]
            
            s = nums[f]
            f = nums[nums[s]]
        
        return -1



