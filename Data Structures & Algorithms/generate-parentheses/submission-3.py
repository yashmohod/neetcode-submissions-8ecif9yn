class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        s = []
        res = []

        def bt(o,c):

            if o == c == n:
                res.append("".join(s))
            
            if o > c:
                s.append(")")
                bt(o,c+1)
                s.pop()
            if o < n:
                s.append("(")
                bt(o+1,c)
                s.pop()

            
        bt(0,0)
        return res