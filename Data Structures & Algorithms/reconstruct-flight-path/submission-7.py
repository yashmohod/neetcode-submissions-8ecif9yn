class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for src, dst in tickets:
            adj.setdefault(src, []).append([dst, 0])
        for k in adj:
            adj[k].sort()

        sofar = ["JFK"]

        def dfs(cur):
            if len(sofar) == len(tickets) + 1:
                return True
            if cur not in adj:
                return False
            for too in adj[cur]:
                if not too[1]:
                    too[1] = 1
                    sofar.append(too[0])
                    if dfs(too[0]):
                        return True
                    sofar.pop()
                    too[1] = 0
            return False

        dfs("JFK")
        return sofar