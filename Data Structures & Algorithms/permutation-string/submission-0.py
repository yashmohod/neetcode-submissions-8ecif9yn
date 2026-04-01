class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        st = {}
        for i in s1:
            st[i] = st.get(i,0)+1

        def check(a,b):
            ans = True
            for i in a.keys():
                if i not in b or a[i] != b[i]:
                    ans=False
            return ans
        
        cp = {}
        for i in range(len(s2)):
            cp[s2[i]] = cp.get(s2[i],0)+1
            if i > len(s1)-1:
                print(s2[i-len(s1):i],s2[i-len(s1)])
                cp[s2[i-len(s1)]] = cp.get(s2[i-len(s1)])-1
            if check(st,cp):
                return True
        return False

