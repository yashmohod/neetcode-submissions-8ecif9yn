class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        


        mem = {0:0}

        def dfs(a):
            if a in mem:
                return mem[a]
            
            res = 1e9
            for c in coins:
                cc = a-c
                if cc >= 0:
                    res = min(res,1+dfs(cc))
            
            mem[a] = res
            return res
        
        t = dfs(amount)
        return -1 if t >= 1e9 else t

                

