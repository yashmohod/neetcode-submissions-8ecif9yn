class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)  # heaviest (most negative)
            b = heapq.heappop(stones)  # second heaviest
            if a != b:
                heapq.heappush(stones, a - b)  # remainder, still negative

        return -stones[0] if stones else 0