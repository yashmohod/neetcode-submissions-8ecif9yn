class Solution:
    def trap(self, height: List[int]) -> int:
        
        som =0
        l,r = 0,len(height)-1

        ml,mr=height[l],height[r]

        while l<r:
            
            if height[l] < height[r]:
                som+= max(0,ml-height[l])
                ml = max(ml,height[l])
                l+=1
            else:
                som+= max(0,mr-height[r])
                mr = max(mr,height[r])
                r-=1

        return som
