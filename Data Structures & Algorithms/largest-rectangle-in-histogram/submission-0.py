class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        area = 0 
        for idx,h in enumerate(heights + [0]):
            start = idx
            while s and h < s[-1][0]:
                lh,lp = s.pop()
                area = max(lh*(idx-lp),area)
                start = lp
            s.append([h,start])           
        return area