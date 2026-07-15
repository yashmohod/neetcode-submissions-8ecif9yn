class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lis = {}
        
        for i in range(len(nums)-1,-1,-1):
            lis[i] = 1
            for k,v in lis.items():
                if nums[k] > nums[i]:
                    lis[i] = max(lis[i],v+1)
        print(lis)
        return max( lis.values())
            

        
     

