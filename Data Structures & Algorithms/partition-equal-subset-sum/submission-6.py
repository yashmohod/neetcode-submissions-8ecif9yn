class Solution:
    def canPartition(self, nums: List[int]) -> bool:
    
        s = sum(nums)
        if s%2 != 0:
            return False
        h = s//2
        mem = {}
        def bt(c, i):
            if c == h: return True
            if c > h or i == len(nums): return False
            if (c,i) in mem: return mem[(c,i)]
            mem[(c,i)] = bt(c, i+1) or bt(c + nums[i], i+1)
            return mem[(c,i)]
            
        return bt(0,0)
                





