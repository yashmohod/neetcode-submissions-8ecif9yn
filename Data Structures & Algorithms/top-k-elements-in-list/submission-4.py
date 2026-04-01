class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bu = [[] for _ in range(len(nums)+1)] 
        nums = Counter(nums)

        for num, freq in nums.items():
            bu[freq].append(num)
        
        res = []
        bc = len(bu)-1
        while len(res)<k:
            if bu[bc]:
               res.append(bu[bc].pop())
            else:
                bc -=1
        return res