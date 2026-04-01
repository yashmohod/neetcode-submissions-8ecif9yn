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
                if not t or t[-1] != check[i]:
                    return False
                else:
                    if t:
                        t.pop()
            else:
                t.append(i)
        
        return len(t) == 0