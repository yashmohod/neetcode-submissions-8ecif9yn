class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lm = float('inf') 
        res = 0 

        for i in range(len(prices)):
            if i > 0:
                res = max(res,prices[i]-lm)
            lm = min(prices[i],lm)

        return res
