class Solution:
    def isValid(self, s: str) -> bool:
        
        check = {
            "}":"{",
            "]":"[",
            ")": "("
        }

        t = deque([])
        for i in s :
            if i in check:
                if t[-1] != check[i]:
                    return False
                else:
                    t.pop()
            else:
                t.append(i)
        
        return len(t) == 0