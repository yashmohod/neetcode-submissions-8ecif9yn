class MinStack:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, val: int) -> None:
        
        if self.stk2:
            self.stk2.append(min(val,self.stk2[-1]))
        else:
            self.stk2.append(val)
        self.stk1.append(val)

    def pop(self) -> None:
        self.stk2.pop()
        return self.stk1.pop()

    def top(self) -> int:
        return self.stk1[-1]

    def getMin(self) -> int:
        return self.stk2[-1]
