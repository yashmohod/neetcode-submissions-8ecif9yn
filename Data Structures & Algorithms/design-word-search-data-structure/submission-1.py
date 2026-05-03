class TD:
    def __init__(self):
        self.children = {}
        self.eof = False
class WordDictionary:

    def __init__(self):
        self.root = TD()

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TD()
            cur = cur.children[ch]
        cur.eof = True

    def search(self, word: str) -> bool:
    
        def dfs(node, idx):
            if idx == len(word):
                return node.eof
            
            if word[idx] == ".":
                return any(dfs(child, idx + 1) for child in node.children.values())
            else:
                if word[idx] not in node.children:
                    return False
                return dfs(node.children[word[idx]], idx + 1)
    
        return dfs(self.root, 0)