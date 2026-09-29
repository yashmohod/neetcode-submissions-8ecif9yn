class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        

        adj ={}
        for ticket in tickets:
            if ticket[0] in adj:
                adj[ticket[0]].append([ticket[1],0])
            else:
                adj[ticket[0]] = [[ticket[1],0]]
        result = []
        resultString = ""
        def dfs(cur,sofar):
            nonlocal result, resultString
            if len(sofar) == len(tickets) :
                print(sofar, len(result) == 0 or resultString > "".join(sofar))
                if len(result) == 0 or resultString > "".join(sofar):
                    result = sofar.copy()
                    resultString = "".join(sofar)
                return
            
            for too in adj[cur]:
                if not too[1]:
                    sofar.append(too[0])
                    too[1]=1
                    dfs(too[0],sofar)
                    too[1]=0
                    sofar.pop()
        
        dfs("JFK",[])
        return ["JFK"]+result
                
        
            

        

