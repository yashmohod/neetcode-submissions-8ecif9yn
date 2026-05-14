class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        tc = Counter(tasks)
        
        h = [-x for x in tc.values()]
        heapq.heapify(h)
        q = deque([])

        t = 0

        while h or q:
            if len(h)>0:
                cur = (-heapq.heappop(h))-1

                if cur >0:
                    q.append((t+n,cur))
            
            while q and q[0][0] <=t:
                t,v = q.popleft()
                heapq.heappush(h,-v)
            
            t+=1
        
        return t