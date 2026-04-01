class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ht = {}

        for i in nums:
            ht[i] = 1+ ht.get(i,0)

        buc = []

        for i in range(len(nums)+1):
            buc.append([])
        
        for val,freq in ht.items():
            # print(freq,val)
            buc[freq].append(val)
        print(buc)
        res = []
        count = 0 
        while k > 0 :
            for i in buc[len(buc)-1-count]:
                res.append(i)
                k-=1
                if k < 1 :
                    return res
            count +=1

