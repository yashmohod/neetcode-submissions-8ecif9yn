class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        def bt(i,s,sofar):
            if s == target:
                res.append(sofar.copy())
                return
            
            if i >= len(candidates) or s > target:
                return
            
            sofar.append(candidates[i])
            bt(i+1,s+candidates[i],sofar)
            sofar.pop()
            bt(i+1,s,sofar)
            return
        
        bt(0,0,[])
        return res


