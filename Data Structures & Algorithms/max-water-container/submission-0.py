class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r = 0,len(heights)-1
        cap = 0
        while l<r:
            cap = max(cap,min(heights[l],heights[r])*(r-l))

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        
        return cap
            
