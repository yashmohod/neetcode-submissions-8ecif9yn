class Solution:
    def canPartition(self, nums: List[int]) -> bool:
    
        s = sum(nums)
        if s%2 != 0:
            return False
        h = s//2
        mem = {}
        def bt(c,i):
            if (c,i) in mem:
                return mem[(c,i)]
            if i < len(nums) and c+nums[i] == h:
                mem[(c,i)] = True
                return True
            if i < len(nums) and c+nums[i] < h:
                res = bt(c,i+1) or bt(c+nums[i],i+1)
                mem[(c,i)] = res
                return res
            if i < len(nums) and c+nums[i] > h:
                res = bt(c,i+1)
                mem[(c,i)] = res
                return res
            mem[(c,i)] = False
            return False
            
        return bt(0,0)
                





