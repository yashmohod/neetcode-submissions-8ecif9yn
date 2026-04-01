class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = []
        ca = [[p,s] for p,s in zip(position,speed)]
        ca.sort(reverse=True)
        
        for cp,cs in ca :

            if len(s) == 0:
                s.append((cp,cs))
            else:
                lp,ls = s[-1]
                lt = (target - lp) / ls
                ct = (target - cp) / cs

                if ct > lt:
                    s.append((cp,cs))
        
        return len(s)