class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # 2 , a , 97

        res = []
        s = []

        def bt(i):

            if i >= len(digits):
                if s :
                    res.append("".join(s.copy()))
                return
            
            for j in range(3):
                s.append(chr((int(digits[i])-2)*3 + 97+j))
                bt(i+1)
                s.pop()
        
        bt(0)
        return res

