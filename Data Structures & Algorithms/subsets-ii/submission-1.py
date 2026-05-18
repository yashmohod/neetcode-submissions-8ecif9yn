class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
       
        res = []
        nums.sort()
        def bt(i,cur):

            if i >= len(nums):
                # cur.sort()
                # if cur not in res:
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            bt(i+1,cur)
            cur.pop()
            j = i+1 
            while j <len(nums) and nums[j] == nums[i]:
                j+=1
            bt(j,cur)
            return
            
        bt(0,[])

        return res