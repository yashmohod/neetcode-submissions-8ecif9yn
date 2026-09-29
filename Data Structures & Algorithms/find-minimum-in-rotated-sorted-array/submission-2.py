class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        if r == 0 :
            return nums[0]
        if nums[0] > nums[-1]: 

            while l<=r:
                m = (r+l)//2
                print(m)
                if nums[m] < nums[(m+1)%len(nums)] and nums[m] < nums[m-1]:
                    return nums[m]
                else :
                    l=m
        else:   
            while l<=r:
                m = (r+l)//2
                print(m)
                if nums[m] < nums[(m+1)%len(nums)] and nums[m] < nums[m-1]:
                    return nums[m]
                else :
                    r=m