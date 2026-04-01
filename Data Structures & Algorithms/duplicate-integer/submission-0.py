class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        h = {}

        for i in nums:
            h[i] = 1 + h.get(i,0)

            if h.get(i) >1:
                return True
        
        return False
        