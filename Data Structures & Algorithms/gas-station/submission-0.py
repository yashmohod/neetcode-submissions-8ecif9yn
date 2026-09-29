class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if len(gas) == 1:
            return 0
        res = float('inf')
        for i in range(len(gas)):
            r = i
            if gas[i] > cost[r]:
                res = min(i,res)
                cost[r], gas[i] = 0, gas[i]-cost[r]
            else:
                cost[r], gas[i] = cost[r]-gas[i],0
        g,c = 0,0
        for i in range(len(gas)):
            g+=gas[i]
            c+=cost[i]
        if c > g:
            return -1

        return res
        