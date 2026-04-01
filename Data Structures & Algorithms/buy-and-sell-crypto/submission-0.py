class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        l,r = 0,0
        pr = 0
        while r<len(prices):

            if prices[r]>prices[l]:
                pr = max(prices[r]-prices[l],pr)
                r+=1
            else:
                l = r
                r = l+1
        
        return pr

