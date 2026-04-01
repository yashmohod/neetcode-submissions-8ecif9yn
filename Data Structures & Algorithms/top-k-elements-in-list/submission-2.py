class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        ht = {}
        for i in nums:
            ht[i] = 1+ ht.get(i,0)
        
        th = {}

        for key in ht:
            if ht[key] in th:
                th[ht[key]].append(key)
            else:
                th[ht[key]] = [key]
        
        res = []

        v = len(nums)
        while v>0 and k>=1:
            for i in th.get(v,[]):
                res.append(i)
                k-=1
                if k < 1:
                    break
            v-=1
        return res

