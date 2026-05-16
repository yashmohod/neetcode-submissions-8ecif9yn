class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(idx,sofar):

            if idx < len(nums):
                sofar.append(nums[idx])
                bt(idx+1,sofar.copy())
                sofar.remove(nums[idx])
                bt(idx+1,sofar.copy())
            else:
                res.append(sofar)
        
        bt(0,[])

        return res




