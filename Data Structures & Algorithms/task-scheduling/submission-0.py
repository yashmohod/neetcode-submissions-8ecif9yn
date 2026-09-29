class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        c = Counter(tasks)
        h = []
        count = -1
        for v in c.values():
            heapq.heappush(h,(count+n,v))
            count+=1
        
        
        while h :
            if h[0][0] == count:
                t,k = heapq.heappop(h)
                k -=1
                if  k > 0 :
                    heapq.heappush(h,(t+n,k))
            count+=1
        return count
        