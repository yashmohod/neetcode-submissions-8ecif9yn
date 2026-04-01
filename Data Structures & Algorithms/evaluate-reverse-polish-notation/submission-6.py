class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = deque([])

        for i in tokens:

            if i == "+":
                b = s.pop()
                a = s.pop()
                s.append(a+b)

            elif i == "-":
                b = s.pop()
                a = s.pop()
                s.append(a-b)

            elif i == "*":
                b = s.pop()
                a = s.pop()
                s.append(a*b) 
            elif i == "/":
                b = s.pop()
                a = s.pop()
                s.append(int(a/b)) 
            else:
                s.append(int(i))
        
        return s[0]