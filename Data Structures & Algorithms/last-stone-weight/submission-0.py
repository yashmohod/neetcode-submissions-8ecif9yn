class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        for i in range(len(stones)):
            stones[i] *=-1
        heapq.heapify(stones)
        cur = None

        while len(stones)>0:
            if cur == None:
                cur = heapq.heappop(stones)
            else:
                t = heapq.heappop(stones)
                cur = min(cur,t) - max(cur,t) if cur != t else 0

        return -cur 