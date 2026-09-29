class Solution:
    def canPartition(self, nums: List[int]) -> bool:
    
        s = sum(nums)
        if s%2 != 0:
            return False
        h = s//2
        def bt(c,i):

            if i < len(nums) and c+nums[i] == h:
                return True
            if i < len(nums) and c+nums[i] < h:
                return bt(c,i+1) or bt(c+nums[i],i+1)
            if i < len(nums) and c+nums[i] < h:
                return bt(c,i+1)
            
        return bt(0,0)
                





