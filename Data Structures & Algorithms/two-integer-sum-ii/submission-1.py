class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r = 0,1

        while r < len(numbers):
            som = numbers[r] + numbers[l]

            if som < target:
                r+=1
            elif som > target:
                l+=1
            elif som == target:
                return[l+1,r+1]
            else:
                print("something went wrong")
                print(l,r)