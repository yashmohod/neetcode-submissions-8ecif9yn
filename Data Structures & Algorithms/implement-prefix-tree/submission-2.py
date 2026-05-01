class TN():
    def __init__(self):
       self.eof = False
       self.children = {} 

class PrefixTree:

    def __init__(self):
        self.root = TN()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TN()
            cur = cur.children[c]
        cur.eof = True

    def search(self, word: str) -> bool:
        cur = self.root
    
        for c in word:
            if not cur:
                return False
            cur = cur.children.get(c,None)
        
        return cur.eof if cur != None else False


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        

        for c in prefix:
            if not cur:
                return False
            cur = cur.children.get(c,None)
        
        return cur != None
       
        