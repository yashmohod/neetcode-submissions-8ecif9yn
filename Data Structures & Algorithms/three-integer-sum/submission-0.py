class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        b ={}
        for i in range(len(nums)):
            b[nums[i]]= i
        res =set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                diff = 0-(nums[i]+nums[j])
                if diff in b and i != j:
                    r = [i,j]
                    if b[diff] in r:
                        continue 
                    r.append(b[diff])
                    d = [nums[i],nums[j],diff]
                    d.sort()
                    res.add(tuple(d))

        return list(res)