class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(i,s,sofar):

            if s == target:
                res.append(sofar.copy())
                return
            if i >= len(nums) or s > target:
                return
            
            sofar.append(nums[i])
            bt(i,s+nums[i],sofar)
            sofar.pop()
            bt(i+1,s,sofar)

            return
        
        bt(0,0,[])
        return res
            

