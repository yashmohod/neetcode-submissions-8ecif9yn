class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        zeros = nums.count(0)
        product = 1
        for i in nums:
            if i !=0:
                product *=i

        res = []
        for i in nums:
            if zeros == 0:
                res.append(product//i)
            elif zeros == 1:
                if i == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(0)
        return res