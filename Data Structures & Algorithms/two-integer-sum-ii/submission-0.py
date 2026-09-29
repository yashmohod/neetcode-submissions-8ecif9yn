class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r = 0,1

        while r < len(numbers):
            diff = numbers[r] + numbers[l]

            if diff < target:
                r+=1
            if diff > target:
                l+=1
            if diff == target:
                return[l+1,r+1]