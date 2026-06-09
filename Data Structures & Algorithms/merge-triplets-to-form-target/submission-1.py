class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        g = set()

        for t in triplets:
            if t[0]>target[0] or t[1]>target[1]  or t[2]>target[2] :
                continue
            
            for i in range(3):
                if target[i] == t[i]:
                    g.add(i)
        return len(g) == 3