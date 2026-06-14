class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        g = {i:[] for i in wordList}
        if endWord not in g:
            return 0 

        def dif(w1,w2):
            d = 0
            for x,y in zip(w1,w2):
                if x!=y:
                    d+=1
            return d
        
        for i in range(len(wordList)):
            for j in range(i,len(wordList)):
                if i != j and dif(wordList[i],wordList[j]) == 1 :
                    g[wordList[i]].append(wordList[j])
                    g[wordList[j]].append(wordList[i])
        
        v = set()
        q = deque()
        q.append((endWord,1))

        while q :
            w,l = q.popleft()
            if dif(w,beginWord) ==1:
                return l+1
            for nw in g[w]:
                if nw not in v:
                    q.append((nw,l+1))
                    v.add(nw)
        return 0