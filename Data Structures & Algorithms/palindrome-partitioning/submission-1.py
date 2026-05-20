class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        res = []
        st = []

        def bt(i):
            if i >= len(s):
                if st :
                    res.append(st.copy())
                return
            
            for j in range(i,len(s)):
                if self.isP(s,i,j):
                    st.append(s[i:j+1])
                    bt(j+1)
                    st.pop()
            return
        bt(0)
        return res
    
    def isP(self,s,i,j):

        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i+=1
                j-=1
        return True