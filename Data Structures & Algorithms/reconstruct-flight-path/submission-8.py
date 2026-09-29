class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for src, dst in tickets:
            if src not in adj:
                adj[src]=[]
            adj[src].append(dst)
        for k in adj:
            adj[k].sort()
            adj[k] = deque(adj[k])
        

        result = []

        def dfs(cur,sofar):
            if len(sofar) == len(tickets) + 1:
                result.append(sofar.copy())
            if cur not in adj:
                return 
            
            cc = adj[cur].copy()
            for i in cc:
                pl = adj[cur].popleft()
                sofar.append(i)
                dfs(i,sofar)
                sofar.pop()
                adj[cur].appendleft(pl)
            
        dfs("JFK",["JFK"])
        result.sort()
        return result[0]


        