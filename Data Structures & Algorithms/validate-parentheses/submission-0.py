class Solution:
    def isValid(self, s: str) -> bool:
        
        s =[]
        l = "[{("

        for i in s:
            if i in l:
                s.append(i)
            else:
                cur = s.pop()
                if i == ')' and cur !="(":
                    return False
                if i == '}' and cur !="{":
                    return False
                if i == ']' and cur !="[":
                    return False
        
        return len(s) ==0

