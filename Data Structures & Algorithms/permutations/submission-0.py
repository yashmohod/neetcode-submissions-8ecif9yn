class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def bt(cur,left):

            if len(left) == 0:
                res.append(cur.copy())
            
            for i in left:
                cur.append(i)
                l = left.copy()
                l.remove(i)
                bt(cur,l)
                cur.remove(i)
        bt([],nums)


        return res