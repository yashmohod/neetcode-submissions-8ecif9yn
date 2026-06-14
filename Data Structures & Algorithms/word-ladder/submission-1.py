class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        if endWord not in wordList:
            return 0 
        g = {}
        for w in wordList:
            for i in range(len(w)):
                k = w[:i]+"*"+w[i+1:]
                if k not in g:
                    g[k] = []
                g[k].append(w)
        
            
        
        v = set()
        q = deque()
        q.append((endWord,1))

        while q :
            w,l = q.popleft()
            for i in range(len(w)):
                k = w[:i]+"*"+w[i+1:] 
                sk = beginWord[:i]+"*"+beginWord[i+1:] 
                if k == sk:
                    return l+1
                for nw in g[k]:
                    if nw not in v:
                        q.append((nw,l+1))
                        v.add(nw)
        return 0
