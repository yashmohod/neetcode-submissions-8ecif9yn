class Solution:
    def trap(self, height: List[int]) -> int:
        ml=[0]*len(height)
        cm=0
        for i in range(1,len(height)):
            cm = max(cm,height[i-1])
            ml[i] = cm
        cm=0
        ans = 0
        for i in range(len(height)-2,-1,-1):
            cm= max(cm,height[i+1])
            ans += min(ml[i],cm) - height[i] if min(ml[i],cm) - height[i]>0 else 0
        return ans 