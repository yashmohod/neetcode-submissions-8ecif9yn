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
        
        def dfs(root,idx):
            if idx > len(word):
                return False
            if word[idx] == ".":
                if idx <= len(word)-1:
                    return True
                else:
                    res = [dfs(root.children[key],idx+1) for key in root.children.keys()]
            else:
                if word[idx]  in root.children:
                    if idx <= len(word)-1:
                        return True
                    else:
                        return dfs(root.children[word[idx]],idx+1)
                else:
                    return False
        
        return dfs(self.root,0)