class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet=0

        seen = set()

        for i in range(len(position)):
            t = (target - position[i])//speed[i]
            if t not in seen:
                seen.add(t)
                fleet +=1
        
        return fleet
            
