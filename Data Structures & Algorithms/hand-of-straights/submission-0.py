class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        c = Counter(hand)
        h = list(c.keys())
        heapq.heapify(h)

        while h:
            m = h[0] 

            for i in range(groupSize):
                if m in c and c[m] >0 :
                    c[m] = c[m] -1
                else:
                    return False
                if c[m] == 0 :
                    heapq.heappop(h)
                m += 1
        
        return True if len(h) == 0 else False
            
        
