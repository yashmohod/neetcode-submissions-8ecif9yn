class Solution:
    def isValid(self, s: str) -> bool:
        
        st =[]
        l = "[{("

        for i in s:
            if i in l:
                st.append(i)
            else:
                if st:
                    cur = st.pop()
                    if i == ")" and cur !="(":
                        return False
                    elif i == "}" and cur !="{":
                        return False
                    elif i == "]" and cur !="[":
                        return False
                else:
                    return False
        
        return len(st) ==0

