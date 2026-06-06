class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        gs=0
        cs=0
        t=0
        res = 0

        for i in range(len(gas)):
            gs+=gas[i]
            cs+=cost[i]
            t += gas[i]-cost[i]

            if t < 0:
                t=0
                res=i+1
        
        return res if gs >= cs else -1
        