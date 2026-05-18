class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
       
        res = []
        nums.sort()
        def bt(i,cur):

            if i >= len(nums):
                cur.sort()
                if cur not in res:
                    res.append(cur.copy())
                return
            
            cur.append(nums[i])
            bt(i+1,cur)
            cur.pop()
            bt(i+1,cur)
            return
            
        bt(0,[])

        return res