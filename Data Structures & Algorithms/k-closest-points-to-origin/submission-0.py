class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        for i in points:
            heapq.heappush(h,((i[0]**2 + i[1]**2)**(0.5),i))

        res = []
        while len(res)<k:
            res.append(heapq.heappop(h)[1])

        return res