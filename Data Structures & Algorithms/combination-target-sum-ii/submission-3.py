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
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue          # skip duplicate at same tree level
                sofar.append(candidates[j])
                bt(j + 1, s + candidates[j], sofar)
                sofar.pop()
            return
        
        bt(0,0,[])
        return res


