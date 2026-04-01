class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [[p,s] for p,s in zip(position,speed)]

        seen = []
        for p,s in sorted(pairs)[::-1]:
            t = ((target - p)/s)
            seen.append(t)
            if len(seen)>=2 and seen[-1]<= seen[-2]:
                seen.pop()        
        return len(seen)
            
