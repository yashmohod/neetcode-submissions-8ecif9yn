class Node:
    def __init__(self,val=None,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.l = {}
        self.capacity = capacity
        self.st = deque([])

    def get(self, key: int) -> int:
        if key in self.l:
            self.st.append(key)
        return self.l.get(key,-1)


    def put(self, key: int, value: int) -> None:
        if len(self.l.keys())+1 > self.capacity:
            del self.l[self.st.popleft()]
        
        self.l[key] = value

            
                