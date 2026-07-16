class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        nt = [-1] * (n+1)
        nt[0] = 0
        aj = {}
        for u,v,t in times:
            if u in aj:
                aj[u].append((v,t))
            else:
                aj[u] = [(v,t)]
            
        q = deque([(k,0)])
        
        while q:
            v,ct = q.popleft()
            if nt[v] > ct or nt[v] == -1:
                nt[v] = ct
                if v in aj:
                    for vv,tt in aj[v]:
                        q.append((vv,tt+ct))

        return max(nt) if -1 not in nt else  -1 


        