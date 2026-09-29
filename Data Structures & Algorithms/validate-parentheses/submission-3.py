class Solution:
    def isValid(self, s: str) -> bool:
        
        check = {
            "}":"{",
            "]":"[",
            ")": "("
        }

        s = deque([])
        for i in s :
            if i in check:
                if s[-1] != check[i]:
                    return False
                else:
                    s.pop()
            else:
                s.append(i)
        
        return True 