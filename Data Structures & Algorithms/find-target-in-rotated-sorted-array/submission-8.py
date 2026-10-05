class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

        while l<r:
            m = (l+r)//2

            if nums[m]>nums[r]:
                l = m+1
            else:
                r=m
        
        p = l 

        if nums[p]> target and nums[0]< target:
            l =0
            r = p-1
        else:
            l=p
            r=len(nums)-1

        while l <=r:
            m = (l+r)//2

            if nums[m]>target:
                r = m-1
            elif nums[m]<target:
                l =m+1
            else:
                return m
        return -1

        