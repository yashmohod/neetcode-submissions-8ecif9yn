class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        b={}
        for idx,val in enumerate(numbers):
            dif = target - val
            if dif in b:
                return [b[dif]+1,idx+1]
            b[val] = idx





